import sys
import os
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

# pytpython3 performance.py [input category]
argv_num = len(sys.argv)
argv_list = sys.argv

'''
for i in range(1, argv_num):
    if (argv_list[i] != "risk_free.csv"):
        print(argv_list[i])
'''
'''
performance_df = pd.DataFrame(columns = ['Name', 'SR_month', 'SR_week',
                                         'Omega_month', 'Omega_week',
                                         'RisknessR_month', 'RisknessR_week'])
'''
performance_df = pd.DataFrame(columns = ['Name', 'SR_month',
                                         'Omega_month', 'RisknessR_month'])

# month from 2013-01-01 to now
month_df = pd.DataFrame(columns = ['Month'])
# date = datetime.datetime.today()
date = datetime.datetime(2019, 5, 31)
index = 1
while date.year >= 2013:
    month_df.loc[index] = [date.strftime("%Y-%m")]
    date = date - relativedelta(months = 1)
    index = index + 1

# week from 2013-01-01 to now
week_df = pd.DataFrame(columns = ['Week'])
# date = datetime.datetime.today()
date = datetime.datetime(2019, 5, 31)
index = 1
while date.year >= 2013:
    week_df.loc[index] = [date.strftime("%Y-%U")]
    date = date - relativedelta(days = 7)
    index = index + 1

# risk free rate
month_rf_df = pd.read_csv("../RiskFree/risk_free_month.csv")
week_rf_df = pd.read_csv("../RiskFree/risk_free_week.csv")

csv_files = []

path = '../ETF/' + argv_list[1] + '/'
for root, direct, file in os.walk(path):
    for f in file:
        if '.csv' in f:
            csv_files.append(os.path.join(path, f))

csv_files.sort()
# for f in csv_files:
#     print(f)


for f in csv_files:
    # print(f)
    etf_df = pd.read_csv(f)
    etf_name = f.split('/')[-1]
    etf_name = etf_name.split('.', 1 )[0]
    # print(etf_name)

    # parse number with ,
    f_parse = np.vectorize(parse_number)
    if (etf_df.iloc[:, 2].dtype.type is np.object_):
        etf_df.iloc[:, 2] = f_parse(etf_df.iloc[:, 2])

    # convert into month return
    month_return_list = []
    month_end_nav = etf_df.iloc[0, 2]
    month_start_nav = 0
    curr_month = 0
    prev_month = 0

    for i in range(len(etf_df.index) - 1):
        curr_month = datetime.datetime.strptime(etf_df.iloc[i, 1]
                                                , '%Y-%m-%d').month
        prev_month = datetime.datetime.strptime(etf_df.iloc[i + 1, 1]
                                                , '%Y-%m-%d').month
        if (curr_month != prev_month):
            month_start_nav = etf_df.iloc[i, 2]
            month_return = round((month_end_nav - month_start_nav) \
                / month_start_nav, 8)
            month_return_list.append(month_return)
            month_end_nav = etf_df.iloc[i + 1 , 2]

    # if the month return of the earliest month is not calculated
    if (curr_month == prev_month):
        month_return = round((month_end_nav - etf_df.iloc[len(etf_df.index) - 1, 2]) \
            / etf_df.iloc[len(etf_df.index) - 1, 2], 8)
        month_return_list.append(month_return)

    month_return_list = np.array(month_return_list)
    month_df[etf_name] = month_return_list


    # convert into week return
    week_return_list = []
    week_end_nav = etf_df.iloc[0, 2]
    week_start_nav = 0
    curr_week = 0
    prev_week = 0

    for i in range(len(etf_df.index) - 1):
        curr_weekday = datetime.datetime.strptime(etf_df.iloc[i, 1],
                                               '%Y-%m-%d').weekday()
        prev_weekday = datetime.datetime.strptime(etf_df.iloc[i + 1, 1],
                                               '%Y-%m-%d').weekday()
        if (curr_weekday < prev_weekday):
            week_start_nav = etf_df.iloc[i, 2]
            week_return = round((week_end_nav - week_start_nav) \
                / week_start_nav, 8)
            week_return_list.append(week_return)
            week_end_nav = etf_df.iloc[i + 1 , 2]

    # if the week return of the earliest week is not calculated
    if (curr_weekday > prev_week):
        week_return = round((week_end_nav - etf_df.iloc[len(etf_df.index) - 1, 2]) \
            / etf_df.iloc[len(etf_df.index) - 1, 2], 8)
        week_return_list.append(week_return)

    week_return_list = np.array(week_return_list)
    week_df[etf_name] = week_return_list

    # using returns from 2016-01 to calculate performance
    month_index = len(month_return_list) - 36
    month_return_list = month_return_list[0:month_index]
    # print(month_return_list)

    # risk-free rate
    rf = month_rf_df['risk_free'][0:month_index]
    adj_return = np.array(month_return_list - rf)
    # print(rf) 
    
    # sharpe ratios
    mu = np.mean(adj_return)
    sigma = math.sqrt((np.var(month_return_list)))
    
    sharpe = mu / sigma
    
    # omega performance measue
    threshold_return = np.array(rf - month_return_list)
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
# write result
month_df.to_csv(argv_list[1] + '/month.csv', index = False)
week_df.to_csv(argv_list[1] + '/week.csv', index = False)

performance_df = performance_df.sort_values(by = 'RisknessR_month', ascending = False)
performance_df.to_csv(argv_list[1] + '/performance.csv', index = False)