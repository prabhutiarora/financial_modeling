from simulator import simulate
import copy
import numpy as np


def run_monte_carlo(
    base_startup,
    runs=1000,
    months=36,
    decisions=None,
    events=None,
    exit_multiple=None,
    discount_rate=0.1
    
):

    survival_count = 0
    exit_values = []
    dcf_values = []
    final_cash_values = []
    final_revenues = []
    investor_return_samples = []

    for _ in range(runs):

        startup_copy = copy.deepcopy(base_startup)

        result = simulate(
            startup_copy,
            months=months,
            decisions=decisions,
            events=events,
            exit_multiple=exit_multiple,
            discount_rate=discount_rate
        )

        summary = result["summary"]

        # Survival
        if not summary["bankrupt"]:
            survival_count += 1

        # Track distributions
        final_cash_values.append(summary["final_cash"])
        final_revenues.append(summary["final_revenue"])
        dcf_values.append(summary["dcf_value"])

        if summary["exit_value"]:
            exit_values.append(summary["exit_value"])

        if summary["investor_returns"]:
            investor_return_samples.extend(
                summary["investor_returns"].values()
            )



    survival_probability = survival_count / runs

    def safe_mean(x):
        return np.mean(x) if len(x) > 0 else 0

    def safe_std(x):
        return np.std(x) if len(x) > 0 else 0

    def var_5(x):
        return np.percentile(x, 5) if len(x) > 0 else 0

    results = {
        "survival_probability": survival_probability,

        # Exit valuation stats
        "expected_exit_value": safe_mean(exit_values),
        "exit_value_std": safe_std(exit_values),
        "exit_value_5th_percentile": var_5(exit_values),

        # DCF stats
        "expected_dcf_value": safe_mean(dcf_values),
        "dcf_std": safe_std(dcf_values),

        # Cash distribution
        "expected_final_cash": safe_mean(final_cash_values),
        "cash_5th_percentile": var_5(final_cash_values),

        # Revenue distribution
        "expected_final_revenue": safe_mean(final_revenues),
        "revenue_std": safe_std(final_revenues),

        # Investor return distribution
        "expected_investor_return": safe_mean(investor_return_samples),
        "investor_return_5th_percentile": var_5(investor_return_samples),
        "final_cash_distribution": final_cash_values,
        "exit_distribution": exit_values
    }

    return results