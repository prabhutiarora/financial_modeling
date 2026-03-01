from montecarlo import run_monte_carlo
import copy


def optimize_hiring(startup, hiring_options, runs=300):

    best_survival = 0
    best_choice = None

    for h in hiring_options:

        test = copy.deepcopy(startup)

        # apply hiring immediately
        test.hire(h)

        mc = run_monte_carlo(test, runs=runs)

        survival = mc["survival_probability"]

        if survival > best_survival:
            best_survival = survival
            best_choice = h

    return best_choice, best_survival