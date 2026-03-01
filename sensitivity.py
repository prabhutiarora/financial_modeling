import numpy as np
from montecarlo import run_monte_carlo
import copy


def sensitivity_analysis(startup, param_name, values, runs=300):

    results = {}

    for val in values:

        test_startup = copy.deepcopy(startup)
        setattr(test_startup, param_name, val)

        mc = run_monte_carlo(test_startup, runs=runs)

        results[val] = mc["survival_probability"]

    return results

def plot_sensitivity(results, param_name):
    import matplotlib.pyplot as plt

    x = list(results.keys())
    y = list(results.values())

    plt.figure()
    plt.plot(x, y)
    plt.xlabel(param_name)
    plt.ylabel("Survival Probability")
    plt.title(f"Sensitivity of Survival to {param_name}")
    plt.show()