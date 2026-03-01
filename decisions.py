# hiring decision
def hire(n_employees):
   
    def apply(startup):
        startup.hire(n_employees)
    return apply


def fire(n_employees):
    
    def apply(startup):
        startup.fire(n_employees)
    return apply


def raise_equity(amount, valuation):

    def apply(startup):
        startup.raise_equity(amount, valuation)
    return apply



def issue_convertible(principal, discount=0.2, cap=None):
   
    def apply(startup):
        startup.issue_convertible(principal, discount, cap)
    return apply



def increase_marketing(new_growth_rate, new_cac=None):
    def apply(startup):
        startup.growth_rate = new_growth_rate
        if new_cac:
            startup.cac = new_cac
    return apply



def cut_fixed_cost(percent):
    def apply(startup):
        startup.fixed_cost *= (1 - percent)
    return apply



def change_pricing(new_price):
    def apply(startup):
        startup.price_per_customer = new_price
    return apply


def pivot(new_growth_rate, new_churn_rate, new_cac):
    
    def apply(startup):
        startup.growth_rate = new_growth_rate
        startup.churn_rate = new_churn_rate
        startup.cac = new_cac
    return apply