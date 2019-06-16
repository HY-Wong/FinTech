### 爬取 ETF 淨值

從33個ETF類別的csv檔中，篩選出inception date在2013年之後有資料的ETF，將篩選結果寫入資料夾中`FilteredETF/[category].csv`，並從Yahoo Finance中抓取ETF調整後收盤價（adjusted close），寫入`[category directory]/[ETF symbol].csv`）。

資料來源：
- [ETF](https://etfdb.com)
- [Yahoo Finance](https://www.federalreserve.gov/data/sloos.htm)

### 執行方法
```
$ python3 ETF.py [input.csv] [output directory for filtered csv] [output directory for ETF]
e.g.
$ python3 ETF.py DevelopedMarket1.csv FilteredETF DevelopedMarket1
```
