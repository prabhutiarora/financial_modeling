import streamlit as st
from core import Startup
from montecarlo import run_monte_carlo
from visualization import plot_cash_over_time

st.title("Startup Survival Simulator")

cash = st.slider("Initial Cash", 100000, 2000000, 500000)
growth = st.slider("Growth Rate", 0.0, 0.2, 0.05)
churn = st.slider("Churn Rate", 0.0, 0.1, 0.03)
cac = st.slider("CAC", 50, 500, 120)

startup = Startup(
    cash=cash,
    revenue=50000,
    price_per_customer=100,
    customers=500,
    fixed_cost=20000,
    variable_cost_rate=0.3,
    headcount=5,
    salary_per_employee=8000,
    growth_rate=growth,
    churn_rate=churn,
    cac=cac,
)

if st.button("Run Monte Carlo"):

    results = run_monte_carlo(startup, runs=500)

    st.write("#Survival Probability")
    st.write(results["survival_probability"])

    st.write("#Expected Exit Value")
    st.write(results["expected_exit_value"])