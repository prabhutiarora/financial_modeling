import matplotlib.pyplot as plt
import numpy as np


def plot_cash_over_time(history):
    cash = [state["cash"] for state in history]

    plt.figure()
    plt.plot(cash)
    plt.xlabel("Month")
    plt.ylabel("Cash")
    plt.title("Cash Over Time")
    plt.axhline(0)
    plt.show()


def plot_burn_over_time(history):
    burn = [state["burn"] for state in history]

    plt.figure()
    plt.plot(burn)
    plt.xlabel("Month")
    plt.ylabel("Burn")
    plt.title("Burn Over Time")
    plt.show()

def plot_survival_distribution(mc_results):
    cash_distribution = mc_results["final_cash_distribution"]

    plt.figure()
    plt.hist(cash_distribution, bins=40)
    plt.xlabel("Final Cash")
    plt.ylabel("Frequency")
    plt.title("Monte Carlo Final Cash Distribution")
    plt.show() 

def survival_curve(base_startup, runs=500, months=36):

    survival_counts = np.zeros(months)

    for _ in range(runs):
        sim = base_startup.copy()

        for m in range(months):
            sim.step()
            if not sim.bankruptcy:
                survival_counts[m] += 1
            else:
                break

    survival_probability = survival_counts / runs

    plt.figure()
    plt.plot(survival_probability)
    plt.xlabel("Month")
    plt.ylabel("Survival Probability")
    plt.title("Survival Probability Over Time")
    plt.show()