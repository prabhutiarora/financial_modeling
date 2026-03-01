## Quantitative Startup Survival & Venture Risk Simulator

A modular financial simulation platform for modeling startup growth,
burn dynamics, survival probability, investor returns, and venture1scale
risk using Monte Carlo simulation.


## Overview

This project simulates:
1.  Startup financial propagation
2.  Hiring & fundraising decisions
3.  Market shocks (demand, CAC, cost spikes)
4.  Liquidity constraints & bankruptcy triggers
5.  Equity dilution
6.  Discounted Cash Flow (DCF) valuation
7.  Monte Carlo survival probability
8.  Strategy comparison
9.  Sensitivity analysis
10. Optimization (maximize survival)
11.  Interactive Streamlit dashboard

It bridges:

Financial Modeling × Risk Simulation × Venture Capital Analytics


## Project Structure

core.py → Startup financial engine\
simulator.py → Scenario simulation engine\
decisions.py → Management decisions\
events.py → External shocks\
montecarlo.py → Monte Carlo engine\
strategy.py → Strategy comparison\
sensitivity.py → Sensitivity analysis\
optimizer.py → Optimization layer\
visualization.py → Plotting utilities\
main.py → Example simulation\
app.py → Streamlit dashboard


##  Core Features

### 1.  Financial Engine

Models1:
Customers , Revenue,   Payroll,  Variable costs,  CAC & churn,
Net income , Cash updates, Bankruptcy trigger

### 2. Decision Modeling

Supports1: 
Hiring (headcount growth), Equity fundraising (with
dilution), Marketing changes, Capital injections

### 3.  Shock Modeling

Supports temporary and permanent shocks1:
Demand collapse, CAC spike, Cost spike, Churn spike

Temporary shocks automatically revert over time.

### 4. Monte Carlo Simulation

Computes1:  
Survival probability, Expected exit value, DCF valuation
distribution, Final cash distribution,  Revenue dispersion, Downside
risk metrics

### 5.  Strategy Comparison

Compare multiple decision strategies under identical conditions.

### 6.   Sensitivity Analysis

Measure survival sensitivity to any parameter.

### 7.   Optimization

Find decision parameters that maximize survival probability.

### 8.   Visualization

Plots1:
Cash over time ,Burn over time, Monte Carlo distribution,
Survival curve

### 9. Streamlit Dashboard

Interactive simulation interface.

Run with:1 streamlit run app.py


##  Installation

pip install numpy matplotlib streamlit pypandoc



## How To Run

Deterministic + Monte Carlo simulation:

python main.py

Run Streamlit dashboard:

streamlit run app.py


<!--## What This Model Captures

1.  Liquidity constraints\
2.  Growth compounding\
3.  Shock propagation\
4.  Timing risk\
5.  Dilution effects\
6.  Profitability vs runway mismatch\
7.  Survival vs intrinsic value distinction
-->
<!-- 
##  Applications

1.   Startup runway planning
2.   Venture capital portfolio modeling
3.     Scenario stress testing
4.   Fundraising strategy evaluation
5.   Academic research (startup survival modeling)
6.   Financial engineering projects
 -->





