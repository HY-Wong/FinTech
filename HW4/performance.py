import sys
import time
import datetime
import math
import pandas as pd
import numpy as np
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def sharpe_ratio(rf, r):

    adj_return = np.array(r - rf)
    mu = np.mean(adj_return)
    sigma = math.sqrt((np.var(r)))
    return mu / sigma

def omega(rf, r):

    mu = np.mean(np.array(r - rf))
    threshold_return = np.array(rf - r)
    if (threshold_return[threshold_return > 0].size == 0):
        return np.nan
    else:
        return mu / np.mean(threshold_return[threshold_return > 0])

def riskness_r(rf, r):

    # newton method
    it = 0
    adj_return = np.array(r - rf)
    mu = np.mean(adj_return)
    x_value = np.sign(mu) * 100
    tol = 1e-8
    while (it <= 500):
        exp_value = 0
        for i in range(len(adj_return)):
            exp_value = exp_value + math.exp(-adj_return[i] * x_value)
        exp_value = exp_value / len(adj_return)
        if (abs(exp_value - 1) < tol):
            break
        gradient_value = 0
        for i in range(len(adj_return)):
            gradient_value = gradient_value + -adj_return[i] * \
                math.exp(-adj_return[i] * x_value)
        gradient_value = gradient_value / len(adj_return)
        x_value = x_value - (exp_value - 1) / gradient_value
        it = it + 1

    return x_value

# python3 performance.py

performance_df = pd.DataFrame(columns = ['Name', 'SR_month', 'Omega_month', 'RisknessR_month'
                                         ,'SR_week', 'Omega_week', 'RisknessR_week'])

# month from 2013-01-01 to now
month_df = pd.read_csv('month.csv')
week_df = pd.read_csv('week.csv')
column_list = list(month_df.columns[1:])
#  print(column_list)

# risk free rate
month_rf_df = pd.read_csv('risk_free_month.csv')
week_rf_df = pd.read_csv('risk_free_week.csv')

for num in range(len(column_list)):

    etf_name = column_list[num]
    month_return_array = np.array(month_df[etf_name])
    week_return_array = np.array(week_df[etf_name])

    # risk-free rate
    month_rf = month_rf_df['risk_free']
    week_rf = week_rf_df['risk_free']
    
    # sharpe ratios
    Sharpe_month = sharpe_ratio(month_rf, month_return_array)
    Sharpe_week = sharpe_ratio(week_rf, week_return_array)
    
    # omega performance measue
    Omega_month = omega(month_rf, month_return_array)
    Omega_week = omega(week_rf, week_return_array)
    
    # riskness index
    RisknessR_month = riskness_r(month_rf, month_return_array)
    RisknessR_week = riskness_r(week_rf, week_return_array)

    performance_df = performance_df.append({'Name': etf_name,
                                            'SR_month': Sharpe_month,
                                            'Omega_month': Omega_month,
                                            'RisknessR_month': RisknessR_month,
                                            'SR_week': Sharpe_week,
                                            'Omega_week': Omega_week,
                                            'RisknessR_week': RisknessR_week},
                                            ignore_index = True)

performance_df.to_csv('performance.csv', index = False)