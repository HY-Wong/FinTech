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

# pytpython3 select_etf

# month from 2013-01-01 to now
month_df = pd.DataFrame(columns = ['Month'])
# date = datetime.datetime.today()
date = datetime.datetime(2019, 5, 31)
index = 1
while date.year >= 2013:
    month_df.loc[index] = [date.strftime("%Y-%m")]
    date = date - relativedelta(months = 1)
    index = index + 1

category_direct = []
categoty_list = []

path = '../Performance/'
for root, direct, file in os.walk(path):
    for d in direct:
        category_direct.append(os.path.join(path, d))

category_direct.sort()
# for d in category_direct:
#     print(d)


for d in category_direct:
    
    month_r_df = pd.read_csv(d + '/month.csv')
    performance_df = pd.read_csv(d + '/performance.csv')

    # select top 25% ETF in each category ranking with RisknessR and 
    # the RisknessR should be greater than 0
    num_etf = 0
    name_list = []
    for num_etf in range(max(math.ceil(len(performance_df) / 4), \
        min(5, len(performance_df)))):
        name_list.append(performance_df['Name'][num_etf])
        if performance_df['RisknessR_month'][num_etf] < 0:
            num_etf = num_etf - 1
            name_list.pop()
            break

    category = d.split('/')[-1]
    # print(category, ' ', num_etf, ' ', name_list)

    # form equally weighted portfolio
    return_df = month_r_df[name_list]
    # print(return_df)
    month_return_list = [0] * len(return_df)
    for name in name_list:
        month_return_list = month_return_list + month_r_df[name]
    month_return_list = month_return_list / len(name_list)
    month_df[category] = np.array(month_return_list)
    # print(month_df)

# write result
month_df.to_csv('month.csv', index = False)
