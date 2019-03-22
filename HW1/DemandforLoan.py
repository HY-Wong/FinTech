import csv
import requests
import sys
import time
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse

# python3 ETF.py [output directory]
num = len(sys.argv)
argv_list = sys.argv

'''
for i in range(1, num):
    print(argv_list[i])
'''

# web crawling
head = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
url = 'https://www.federalreserve.gov/data/sloos/sloos-201901-chart-data.htm'
html = requests.get(url, headers = head)

CILoans_df = pd.DataFrame(columns = ['Period', 'Large and Medium', 'Small'])
curr_index = 0

# check if download suceeds
if html.status_code == requests.codes.ok:
    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.prettify())
    trs = soup.find_all('tr')
        
    for tr in trs:
        th = tr.find('th', headers = "F1T")
        if th is not None:
            curr_index = curr_index + 1
            time = th.string.split(':', 1)
            # convert year:quarter into yyyy-mm
            date = datetime.date(int(time[0]) , int(time[1]) * 3 - 2, 1)
            tds = tr.find_all('td', limit = 2)
            CILoans_df.loc[curr_index] = [date.strftime("%Y-%m"), tds[0].string, tds[1].string]

# write the data frame into a csv file
CILoans_df.to_csv(argv_list[1] + '/' + 'C&I Loans.csv')
