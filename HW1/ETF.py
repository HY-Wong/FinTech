import csv
import requests
import sys
import time
import datetime
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

def url_convert(etf_string, dt1, dt2):
    # convert date to time stamp
    p1 = int(time.mktime(dt1.timetuple()))
    p2 = int(time.mktime(dt2.timetuple()))
    url = 'https://finance.yahoo.com/quote/' + etf_string + '/history?period1=' + \
          str(p1) + '&period2=' + str(p2) + '&interval=1d&filter=history&frequency=1d'
    return(url)

# python3 ETF.py [input.csv] [output.csv] [output directory]
num = len(sys.argv)
argv_list = sys.argv

'''
for i in range(1, num):
    print(argv_list[i])
'''

# filter the ETFs
toSave = [] 
with open(argv_list[1], newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    for row in rows:
        ts = datetime.datetime.strptime(row['Inception'], '%d/%m/%Y')
        if ts.year < 2016:
            toSave.append(row)
                
# write the ETFs into a csv file 
with open(argv_list[2], 'w') as csvfile:
    fieldnames = toSave[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(toSave)

# dates for web crawling
date_list = []
start = datetime.date(2019, 1, 1)
date_list.append(start)
date_list.append(datetime.datetime.today())
while start.year >= 2016:
    end = start - relativedelta(days = 1)
    start = start - relativedelta(months = 4)
    date_list.append(start)
    date_list.append(end)
'''
for d in date_list:
    print(d)
'''

# web crawling
head = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
df = pd.read_csv(argv_list[2])
row_num = df['Symbol'].count()

for i in range(row_num):
    # save the ETF data into dataframe
    ETF_df = pd.DataFrame(columns = ['Date', 'NAV'])
    curr_index = 0
    
    for j in range(int(len(date_list) / 2)):
        url = url_convert(df.at[i, 'Symbol'], date_list[2 * j], date_list[2 * j + 1])
        # print(url)
        html = requests.get(url, headers = head)

        # check if download suceeds
        if html.status_code == requests.codes.ok:
            soup = BeautifulSoup(html.text, 'html.parser')
            trs = soup.find_all('tr')
            num_of_date = int(len(trs))
            
            # print(num_of_date)
            num_row = 0
            for k in range(1, num_of_date):
                # write NAV into dataframe excluding dividend
                if len(trs[k]) == 7:
                    num_row = num_row + 1
                    tds = trs[k].find_all('td')
                    date_temp = parse(tds[0].string)
                    ETF_df.loc[curr_index + num_row] = [date_temp.strftime("%Y-%m-%d"), tds[5].string]
            curr_index = curr_index + num_row
    
    # write dataframe into a csv file
    ETF_df.to_csv(argv_list[3] + '/' + df.at[i, 'Symbol'] + '.csv')
