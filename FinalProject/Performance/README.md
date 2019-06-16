### 計算月報酬率、周報酬率與績效

從`../ETF/[category directory]`中讀取ETF調整後收盤價（adjusted close），計算月報酬率並寫入`[category directory]/month.csv`，計算週報酬率並寫入`[category directory]/week.csv`，並根據月報酬率計算ETF績效，寫入`[category directory]/performance.csv`。

### 績效指標
- Sharpe Raio
- Omega: 2011. Omega performance measure and portfolio insurance
- Riskness R: 2013. A global index of riskiness <br />
註：「Generalized Sharpe Ratios: 2009. Portfolio performance evaluation with generalized Sharpe ratios: Beyond the mean and variance」計算條件很多檔ETF之月報酬資料皆不滿足，因此採用傳統之Sharpe Ratio。

### 執行方法
```
$ python3 performance.py [input category]
e.g.
$ python3 performance.py DevelopedMarket1
```
