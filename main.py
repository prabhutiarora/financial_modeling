
from core import Startup
from simulator import simulate
from montecarlo import run_monte_carlo
from decisions import (
    hire,
    raise_equity,
    increase_marketing
)
from events import demand_shock, cac_spike


startup = Startup(
    cash=500_000,
    revenue=50_000,
    price_per_customer=100,
    customers=500,
    fixed_cost=20_000,
    variable_cost_rate=0.3,
    headcount=5,
    salary_per_employee=8,
    growth_rate=0.12,
    churn_rate=0.03,
    cac=120,
    revenue_volatility=2_000
)


decisions = {
    3: [hire(3)],  # hire 3 employees
    6: [raise_equity(800_000, valuation=3_000_000)],  #proper dilution
    10: [increase_marketing(0.08, new_cac=150)]
}




events = {
    5: [demand_shock(0.6, 0.8)],   # demand collapse
    8: [cac_spike(1.5, duration=3)]  # marketing inefficiency
}


result = simulate(
    startup,
    months=24,
    decisions=decisions,
    events=events,
    exit_multiple=6,      # assume 6x revenue exit
    discount_rate=0.12
)

print("\n    DETERMINISTIC SCENARIO     \n")

for month, state in enumerate(result["history"], start=1):
    print(f"Month {month}: {state}")

print("\n   SUMMARY     \n")
for key, value in result["summary"].items():
    print(f"{key}: {value}")


mc_results = run_monte_carlo(
    base_startup=startup,
    runs=1000,
    months=24,
    decisions=decisions,
    events=events,
    exit_multiple=6,
    discount_rate=0.12
)

print("\n   MONTE CARLO RESULTS     \n")
for key, value in mc_results.items():
    print(f"{key}: {value}")


from visualization import (
    plot_cash_over_time,
    plot_burn_over_time,
    plot_survival_distribution
)

# After deterministic simulation
plot_cash_over_time(result["history"])
plot_burn_over_time(result["history"])

# After Monte Carlo
plot_survival_distribution(mc_results)