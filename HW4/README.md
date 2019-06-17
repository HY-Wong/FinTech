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

|	ETF Name  |	month	   |
|	----------|:--------:|
|	ACWV	    |	0.2816	 |
|	JXI	      |	0.2551	 |
|	GII	      |	0.2477	 |
|	IGF	      |	0.2346	 |
|	SMH     	|	0.2230 	 |
|	CGW	      |	0.2069	 |
|	IDLV	    |	0.1830	 |
|	DWX	      |	0.1802	 |
|	IOO	      |	0.1670	 |
|	GUNR	    |	0.1582	 |

|	ETF Name	|	week   	 |
|	----------|:--------:|
|	MOO	      |	0.1177	 |
|	ACWV	    |	0.1108	 |
|	SMH	      |	0.1058	 |
|	PSP	      |	0.1006	 |
|	IDLV	    |	0.0949	 |
|	GII	      |	0.0932	 |
|	IOO	      |	0.0913	 |
|	ACWI	    |	0.0887	 |
|	IGF	      |	0.0864	 |
|	MXI	      |	0.0849	 |


- Omega


- Riskness R


### 執行方法
```
$ python3 performance.py
```
