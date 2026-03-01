import random
import numpy as np
from dataclasses import dataclass, field


@dataclass
class ConvertibleNote:
    principal: float
    discount: float = 0.2
    cap: float = None
    converted: bool = False


@dataclass
class Startup:

    cash: float
    revenue: float
    price_per_customer: float
    customers: int

    fixed_cost: float
    variable_cost_rate: float
    headcount: int
    salary_per_employee: float

    growth_rate: float
    churn_rate: float
    cac: float
    revenue_volatility: float = 0.0


    receivable_days: int = 30
    payable_days: int = 30

   
    shares_outstanding: float = 1_000_000
    investors_equity: dict = field(default_factory=dict)
    convertible_notes: list = field(default_factory=list)

  
    bankruptcy: bool = False
    history: list = field(default_factory=list)


    def hire(self, n):
        self.headcount += n

    def fire(self, n):
        self.headcount = max(0, self.headcount - n)

    def raise_equity(self, amount, valuation):
        new_shares = amount / valuation * self.shares_outstanding
        self.shares_outstanding += new_shares
        self.cash += amount
        self.investors_equity[f"Investor_{len(self.investors_equity)+1}"] = new_shares

    def issue_convertible(self, principal, discount=0.2, cap=None):
        self.cash += principal
        self.convertible_notes.append(ConvertibleNote(principal, discount, cap))



    def acquire_customers(self):
        new_customers = int(self.revenue * self.growth_rate / self.price_per_customer)
        acquisition_cost = new_customers * self.cac
        self.customers += new_customers
        return acquisition_cost

    def apply_churn(self):
        churned = int(self.customers * self.churn_rate)
        self.customers -= churned

    def update_revenue(self):
        self.revenue = self.customers * self.price_per_customer
        shock = random.gauss(0, self.revenue_volatility)
        self.revenue += shock

    def compute_costs(self):
        payroll = self.headcount * self.salary_per_employee
        variable_cost = self.revenue * self.variable_cost_rate
        total_cost = payroll + self.fixed_cost + variable_cost
        return payroll, variable_cost, total_cost

    def working_capital_effect(self):
        receivables = self.revenue * (self.receivable_days / 30)
        payables = self.fixed_cost * (self.payable_days / 30)
        return receivables - payables

    def step(self):
        if self.bankruptcy:
            return

        self._handle_reversions()
        # Customer dynamics
        acquisition_cost = self.acquire_customers()
        self.apply_churn()
        self.update_revenue()

        # Costs
        payroll, variable_cost, total_cost = self.compute_costs()
        wc_change = self.working_capital_effect()

        net_income = self.revenue - total_cost - acquisition_cost
        self.cash += net_income - wc_change

        # Bankruptcy trigger
        if self.cash <= 0:
            self.bankruptcy = True

        snapshot = {
            "cash": self.cash,
            "revenue": self.revenue,
            "net_income": net_income,
            "burn": -net_income if net_income < 0 else 0,
            "customers": self.customers,
            "bankrupt": self.bankruptcy
        }

        self.history.append(snapshot)
        return snapshot


    def ltv(self):
        if self.churn_rate == 0:
            return float("inf")
        return self.price_per_customer / self.churn_rate

    def ltv_cac_ratio(self):
        return self.ltv() / self.cac

    def dcf_valuation(self, discount_rate=0.1, years=5):
        future_cashflows = []
        temp_revenue = self.revenue

        for t in range(1, years+1):
            temp_revenue *= (1 + self.growth_rate)
            fcf = temp_revenue * (1 - self.variable_cost_rate)
            discounted = fcf / ((1 + discount_rate) ** t)
            future_cashflows.append(discounted)

        return sum(future_cashflows)

    def monte_carlo_survival(self, simulations=500, months=36):
        survive = 0

        for _ in range(simulations):
            sim = self.copy()
            for _ in range(months):
                sim.step()
                if sim.bankruptcy:
                    break
            if not sim.bankruptcy:
                survive += 1

        return survive / simulations

    def copy(self):
        import copy
        return copy.deepcopy(self)
    
    def _handle_reversions(self):

    # Churn reversion
        if hasattr(self, "_churn_reversion"):
            for item in self._churn_reversion[:]:
                item["months_left"] -= 1
                if item["months_left"] <= 0:
                    self.churn_rate = item["original"]
                    self._churn_reversion.remove(item)

        # CAC reversion
        if hasattr(self, "_cac_reversion"):
            for item in self._cac_reversion[:]:
                item["months_left"] -= 1
                if item["months_left"] <= 0:
                    self.cac = item["original"]
                    self._cac_reversion.remove(item)

        # Cost reversion
        if hasattr(self, "_cost_reversion"):
            for item in self._cost_reversion[:]:
                item["months_left"] -= 1
                if item["months_left"] <= 0:
                    self.variable_cost_rate -= item["increase"]
                    self._cost_reversion.remove(item)