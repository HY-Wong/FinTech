## ETF爬蟲程式

### 程式說明
從input.csv檔中讀取ETF清單，篩選出inception date在2015年之前的ETF，將篩選結果寫入output.csv。從Yahoo Finance中抓取ETF自2015年底最後一個交易日至今天的調整後收盤價(adjusted close)，存寫入[directory]/XXX.csv(XXX為某檔ETF symbol)。

資料來源：
- [ETF](https://etfdb.com)
- [Yahoo Finance](https://www.federalreserve.gov/data/sloos.htm)

### 執行方法
```
$ python3 ETF.py [input.csv] [output.csv] [directory]
e.g.
$ python3 ETF.py DevelopedMarketsETF24.csv ETF24.csv ETF24
```

### 流程圖
### 套件使用與注意事項
- csv
csv檔的讀取與寫入
- date, datetime
日期格式的處理
- requests, bs4
抓取與解析網頁資料
- dateutil.parser, dateutil.relativedelta
解析字串轉成datetime格式，用於處理自Yahoo Finace抓取的日期字串
- pandas
將抓取的資料存入DataFrame，並將DataFrame寫入csv檔

## 財金指標爬蟲程式

### 程式說明
從美國聯邦準備理事會網站抓取資「國內銀行緊縮企業貸款標準淨比例」資料，依公司大小分為大型與中型(large and medium)和小型(small)兩欄資料，寫入[directory]/C&ILoad.csv。

資料來源：
- [美國聯邦準備理事會](https://www.federalreserve.gov/data/sloos.htm)


### 執行方法
```
$ python3 DemandforLoan.py [directory]
e.g.
$ python3 DemandforLoan.py FinancialIndicator
```

### 流程圖
### 注意事項
