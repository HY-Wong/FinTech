## ETF爬蟲程式

### 程式說明
從DevelopedMarketsETF24.csv檔中讀取ETF清單，篩選出inception date在2015年之前的ETF，將篩選結果寫入output.csv。從Yahoo Finance中抓取ETF自2015年底最後一個交易日至今天的調整後收盤價(adjusted close)。

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
### 注意事項

## 財金指標爬蟲程式

### 程式說明
從美國聯邦準備理事會網站抓取資「國內銀行緊縮企業貸款標準淨比例」資料，依公司大小分為大型與中型(large and medium)和小型(small)兩欄資料。

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
