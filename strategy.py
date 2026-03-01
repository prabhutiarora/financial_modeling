
from montecarlo import run_monte_carlo


def compare_strategies(startup, strategies, runs=500, months=36, events=None):
   
    results = {}

    for name, decisions in strategies.items():

        mc = run_monte_carlo(
            base_startup=startup,
            runs=runs,
            months=months,
            decisions=decisions,
            events=events,
            exit_multiple=6
        )

        results[name] = mc

    return results
