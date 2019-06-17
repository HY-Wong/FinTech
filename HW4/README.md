### 計算績效

`DevekopedMarket1`中ETF的月報酬率存於`month.csv`，週報酬率存於`week.csv`，無風險利率的月資料存於`risk_free_month.csv`，週資料存於`risk_free_week.csv`。三種績效指標計算後的結果寫入`performance.csv`。

### 績效指標
- Sharpe Raio
- Omega: 2011. Omega performance measure and portfolio insurance
- Riskness R: 2013. A global index of riskiness <br />
註：「Generalized Sharpe Ratios: 2009. Portfolio performance evaluation with generalized Sharpe ratios: Beyond the mean and variance」計算條件很多檔ETF之月報酬資料皆不滿足，因此採用傳統之Sharpe Ratio。

### 績效指標排序
檢視三個指標排序前十高的資料
- Sharpe Raio

|	ETF Name	  |	month	   | ETF Name	  |	week	   |
|	----------	|:--------:| ----------	|:--------:|
|	ACWV	      |	0.281595 |	MOO	      |	0.117731 |
|	JXI	        |	0.255117 |	ACWV	    |	0.110826 |
|	GII	        |	0.247696 |	SMH	      |	0.105764 |
|	IGF	        |	0.234607 |	PSP	      |	0.100556 |
|	SMH	        |	0.222961 |	IDLV	    |	0.094918 |
|	CGW	        |	0.206940 |	GII	      |	0.093190 |
|	IDLV	      |	0.183001 |	IOO	      |	0.091263 |
|	DWX	        |	0.180177 |	ACWI	    |	0.088721 |
|	IOO	        |	0.167044 |	IGF	      |	0.086401 |
|	GUNR	      |	0.158204 |	MXI	      |	0.084878 |

前十名中有6檔ETF相同，造成排序不一致的主因為月報酬率的波動度與週報酬率的波動度。
- Omega


- Riskness R


### 執行方法
```
$ python3 performance.py
```
