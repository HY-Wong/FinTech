import sys
import time
import datetime
import pandas as pd
import numpy as np
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def average(lst): 
    return round(sum(lst) / len(lst) / 100, 4)

# pytpython3 performance.py [risk_free.csv]
argv_num = len(sys.argv)
argv_list = sys.argv

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


rf_df = pd.read_csv(argv_list[1])

# convert into month risk free rate
month_rf_list = []
month_rf = []
curr_month = -1
next_month = datetime.datetime.strptime(rf_df.iloc[0, 0]
                                            , '%Y/%m/%d').month

for i in range(len(rf_df.index)): 
    curr_month = datetime.datetime.strptime(rf_df.iloc[i, 0]
                                            , '%Y/%m/%d').month
    month_rf.append(rf_df.iloc[i, 1]) 
    if (curr_month != next_month):
        month_rf_list.append(average(month_rf) / 12)
        month_rf.clear()
    next_month = curr_month

if month_rf:
    month_rf_list.append(average(month_rf) / 12)
    month_rf.clear()
month_df['risk_free'] = month_rf_list

# convert into week risk free rate
week_rf_list = []
week_rf = []
curr_weekday = 8
next_weekday = 8

for i in range(len(rf_df.index)):
    curr_weekday = datetime.datetime.strptime(rf_df.iloc[i, 0],
                                                   '%Y/%m/%d').weekday()
    if (curr_weekday > next_weekday):
        week_rf_list.append(average(week_rf) / 52)
        week_rf.clear()
    week_rf.append(rf_df.iloc[i, 1])
    next_weekday = curr_weekday
    
if week_rf:
    week_rf_list.append(average(week_rf) / 52)
    week_rf.clear()
week_df['risk_free'] = week_rf_list

# write result
month_df.to_csv('risk_free_month.csv', index = False)
week_df.to_csv('risk_free_week.csv', index = False)
