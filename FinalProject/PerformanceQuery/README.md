## 功能實作一

### 類別績效查詢
查詢任一ETF類別中，查詢2013年1月至2019年5月間任一區間各檔ETF的績效，指定以其中一種績效衡量指標排序，寫入`query_performance.csv`。

### 績效指標
- Sharpe Ratio
- Omega
- Riskness R

### 執行方法
```
$ python3 query_performance.py [category] [start_year_month] [end_year_month] [sorting_index]
e.g.
$ python3 query_performance.py DevelopedMarket1 2016-01 2018-12 RisknessR_month
```
