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

月報酬率計算的績效與週報酬率計算的績效有六檔ETF重複，造成排序不一致的主因為月報酬率的波動度與週報酬率的波動度。

- Omega

|	ETF Name	  |	month	   | ETF Name	  |	week	   |
|	----------	|:--------:| ----------	|:--------:|
|	JXI	        |	0.322320 |	ACWV	    |	0.155851 |
|	GII	        |	0.318931 |	MOO	      |	0.141374 |
|	ACWV	      |	0.314072 |	SMH	      |	0.138356 |
|	IGF	        |	0.289947 |	PSP	      |	0.130681 |
|	SMH	        |	0.268688 |	IDLV	    |	0.124954 |
|	CGW	        |	0.247431 |	GII	      |	0.116643 |
|	IDLV	      |	0.226620 |	IOO	      |	0.115600 |
|	GUNR	      |	0.221755 |	ACWI	    |	0.115334 |
|	DWX	        |	0.220939 |	MXI	      |	0.111887 |
|	GDX	        |	0.214332 |	DWX	      |	0.110755 |

月報酬率計算的績效與週報酬率計算的績效有五檔ETF重複；分別比較月報酬率計算的Sharpe Ratio與Omega的排序結果，可以見到兩者結果類似，推測因為兩者公式的分母部分隱含類似概念，即波動度大的ETF，Omega分母值也可能比較大。

- Riskness R

|	ETF Name	  |	month	   | ETF Name	  |	week	   |
|	----------	|:--------:| ----------	|:--------:|
|	ACWV	      |	21.664816| ACWV	      | 18.993788|
|	GII	        |	17.257900| IDLV	      |	13.981397|
|	IGF	        |	16.190371| MOO	      |	13.520821|
|	JXI	        |	14.751624| GII      	|	12.798624|
|	IDLV      	|	13.837544| IGF 	      |	11.683256|
|	DWX	        |	13.048801| IOO	      |	11.118427|
|	CGW	        |	12.153817| ACWI	      |	10.907773|
|	IOO	        |	10.155024| PSP	      |	10.812160|
|	EFAV	      |	9.864899 | CGW      	|	10.602361|
|	ACWI	      |	9.042962 | VT       	|	10.379863|

月報酬率計算的績效與週報酬率計算的績效有七檔ETF重複；比較Sharpe Ratio、Omega與Riskness R的排序結果，可發現相似程度不低。

### 執行方法
```
$ python3 performance.py
```
