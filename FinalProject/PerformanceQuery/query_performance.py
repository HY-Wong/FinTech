import sys
import time
import datetime
import math
import pandas as pd
import numpy as np
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def parse_number(num):
    num = num.replace(',', '')
    return float(num)

# python3 query_performance.py [category] [start_year_month] [end_year_month] [sorting_index]
argv_num = len(sys.argv)
argv_list = sys.argv

performance_df = pd.DataFrame(columns = ['Name', 'SR_month',
                                         'Omega_month', 'RisknessR_month'])

# month from 2013-01-01 to now
month_df = pd.read_csv('../performance/' + argv_list[1] + '/month.csv')
start_year = int(argv_list[2].split('-', 1 )[0])
start_month = int(argv_list[2].split('-', 1 )[1])
start_index = (start_year - 2013) * 12 + start_month
end_year = int(argv_list[3].split('-', 1 )[0])
end_month = int(argv_list[3].split('-', 1 )[1])
end_index = (end_year - 2013) * 12 + end_month
column_list = list(month_df.columns[1:])
#  print(column_list)

# risk free rate
month_rf_df = pd.read_csv("../RiskFree/risk_free_month.csv")

# for num in range(1, len(month_df.columns)):
for num in range(len(column_list)):

    etf_name = column_list[num]
    month_return_list = month_df[etf_name]
    len_return = len(month_return_list)
    # print(month_df['Month'][len_return - end_index:len_return - (start_index - 1)])
    month_return_array = np.array(month_return_list[len_return - end_index: \
        len_return - (start_index - 1)])

    # risk-free rate
    rf = month_rf_df['risk_free'].iloc[len_return - end_index: \
        len_return - (start_index - 1)]
    adj_return = np.array(month_return_array - rf)
    # print(adj_return)
    
    # sharpe ratios
    mu = np.mean(adj_return)
    sigma = math.sqrt((np.var(month_return_array)))
    
    sharpe = mu / sigma
    
    # omega performance measue
    threshold_return = np.array(rf - month_return_array)
    if (threshold_return[threshold_return > 0].size == 0):
        Omega = np.nan
    else:
        Omega = mu / np.mean(threshold_return[threshold_return > 0])
    
    # riskness index
    # newton method
    it = 0
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

    RisknessR = x_value

    performance_df = performance_df.append({'Name': etf_name,
                                            'SR_month': sharpe,
                                            'Omega_month': Omega,
                                            'RisknessR_month': RisknessR},
                                            ignore_index = True)

performance_df = performance_df.sort_values(by = argv_list[4], ascending = False)
performance_df.to_csv('query_performance.csv', index = False)
