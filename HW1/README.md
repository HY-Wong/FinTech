## ETF爬蟲程式

### 程式說明
從`input.csv`檔中讀取ETF清單，篩選出inception date在2015年之前的ETF，將篩選結果寫入`output.csv`。從Yahoo Finance中抓取ETF自2015年底最後一個交易日至今天的調整後收盤價（adjusted close），寫入`[directory]/XXX.csv`（XXX為某檔ETF的symbol）。

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

### 套件使用
- csv\
csv檔的讀取與寫入
- date, datetime\
日期格式的處理
- requests, bs4\
抓取與解析網頁資料
- dateutil.parser, dateutil.relativedelta\
解析字串轉成datetime格式，用於處理自Yahoo Finace抓取的日期字串
- pandas\
將抓取的資料存入DataFrame，並將DataFrame寫入csv檔

### 注意事項
- 下載`ETF.py`以及`DevelopedMarketsETF24.csv`或`DevelopedMarketsETF25.csv`，打開終端機將工作目錄（working directory）切換至檔案存放的目錄即可執行程式
- 須自行建立欲將資料寫進的目錄（`[directory]`）
- Yahoo Finance搜尋區間需將日期（YYYY-MM-DD）轉成timestamp
- Yahoo Finance在抓取資料時一次只能抓取到約6個月的資料，程式內使用4個月為一次抓取之區間
- 少數幾檔ETF抓取資料並不完整，原因不清楚

## 財金指標爬蟲程式

### 程式說明
從美國聯邦準備理事會網站抓取資「國內銀行緊縮企業貸款標準淨比例」資料，依公司大小分為大型與中型(large and medium)和小型(small)兩欄資料，寫入`[directory]/C&ILoad.csv`。

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
- 下載`DemandforLoan.py`，打開終端機將工作目錄（working directory）切換至檔案存放的目錄即可執行程式
- 須自行建立欲將資料寫進的目錄（`[directory]`）
- 聯邦理事會每年於一月、四月或五月、八月、十月或十一月公布資料，此程式於2019年1月公布的表格中抓取資料
