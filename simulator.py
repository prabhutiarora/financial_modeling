import copy
import numpy as np


def simulate(
    startup,
    months=36,
    decisions=None,
    events=None,
    exit_multiple=None,
    discount_rate=0.1,
    stop_on_bankruptcy=True
):
   

    history = []
    startup = copy.deepcopy(startup)

    for month in range(months):

       
        if decisions and month in decisions:
            for decision in decisions[month]:
                decision(startup)

     
        if events and month in events:
            for event in events[month]:
                event(startup)

  
        state = startup.step()

        if state is None:
            break

        history.append(state)

        # Bankruptcy trigger
        if stop_on_bankruptcy and startup.bankruptcy:
            break

    exit_value = None
    investor_returns = {}

    if exit_multiple and not startup.bankruptcy:
        exit_value = startup.revenue * exit_multiple

        for investor, shares in startup.investors_equity.items():
            ownership = shares / startup.shares_outstanding
            investor_returns[investor] = ownership * exit_value

   
    dcf_value = startup.dcf_valuation(discount_rate=discount_rate)

    summary = {
        "final_cash": startup.cash,
        "final_revenue": startup.revenue,
        "bankrupt": startup.bankruptcy,
        "exit_value": exit_value,
        "dcf_value": dcf_value,
        "investor_returns": investor_returns,
        "ltv_cac_ratio": startup.ltv_cac_ratio(),
        "months_simulated": len(history)
    }

    return {
        "history": history,
        "summary": summary
    }

def monte_carlo_simulation(
    startup,
    simulations=500,
    months=36,
    decisions=None,
    events=None,
    exit_multiple=None
):
    survival_count = 0
    exit_values = []
    dcf_values = []

    for _ in range(simulations):

        result = simulate(
            startup,
            months=months,
            decisions=decisions,
            events=events,
            exit_multiple=exit_multiple
        )

        if not result["summary"]["bankrupt"]:
            survival_count += 1

        if result["summary"]["exit_value"]:
            exit_values.append(result["summary"]["exit_value"])

        dcf_values.append(result["summary"]["dcf_value"])

    survival_probability = survival_count / simulations

    return {
        "survival_probability": survival_probability,
        "expected_exit_value": np.mean(exit_values) if exit_values else 0,
        "expected_dcf_value": np.mean(dcf_values),
        "exit_value_std": np.std(exit_values) if exit_values else 0
    }