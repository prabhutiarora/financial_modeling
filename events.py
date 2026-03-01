
import random



def demand_shock(min_drop=0.7, max_drop=0.9):
    
    def apply(startup):
        shock = random.uniform(min_drop, max_drop)
        startup.customers = int(startup.customers * shock)
    return apply


def churn_spike(extra_churn=0.05, duration=3):
    def apply(startup):
        original_churn = startup.churn_rate
        startup.churn_rate += extra_churn

        # Schedule automatic reversion
        if not hasattr(startup, "_churn_reversion"):
            startup._churn_reversion = []

        startup._churn_reversion.append(
            {"months_left": duration, "original": original_churn}
        )

    return apply



def cac_spike(multiplier=1.5, duration=3):
    def apply(startup):
        original_cac = startup.cac
        startup.cac *= multiplier

        if not hasattr(startup, "_cac_reversion"):
            startup._cac_reversion = []

        startup._cac_reversion.append(
            {"months_left": duration, "original": original_cac}
        )

    return apply


def cost_spike(rate_increase=0.05, duration=None):
    def apply(startup):
        startup.variable_cost_rate += rate_increase

        if duration:
            if not hasattr(startup, "_cost_reversion"):
                startup._cost_reversion = []

            startup._cost_reversion.append(
                {
                    "months_left": duration,
                    "increase": rate_increase
                }
            )

    return apply




def salary_inflation(percent_increase=0.1):
    def apply(startup):
        startup.salary_per_employee *= (1 + percent_increase)
    return apply




def funding_freeze():
    def apply(startup):
        startup.can_raise = False
    return apply

def black_swan(severity=0.5):
    def apply(startup):
        startup.customers = int(startup.customers * (1 - severity))
        startup.cash *= (1 - severity)
    return apply



