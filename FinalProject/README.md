## 如何選取好的 ETF

### 資料夾說明

- `ETF`：從33個ETF類別的csv檔中，篩選出inception date在2013年之後有資料的ETF，抓取ETF調整後收盤價（adjusted close）。

- `Perfomance`：利用`ETF`中各檔ETF調整後收盤價（adjusted close），計算月報酬率、週報酬率與ETF績效。

- `PerfomanceQuery`：查詢任一ETF類別中，查詢2013年1月至2019年5月間任一區間各檔ETF的績效，指定以其中一種績效衡量指標排序。

- `Portfolio`：利用33個ETF類別形成的類別ETF標的，任選類別，計算最適配置權重。

- `RiskFree`：計算 U.S. 10 Year Treasury 月資料與週資料。

資料來源：
- [ETF](https://etfdb.com)
- [Yahoo Finance](https://www.federalreserve.gov/data/sloos.htm)
- [U.S. 10 Year Treasury](https://www.cnbc.com/quotes/?symbol=US10Y)

### ETF 類別
Alternatives BroadAsia Commodity ConsumerDiscretionaryEquity ConsumerStaplesEquity <br />
CrudeOil Currency DevelopedAsiaPacific DevelopedEurope DevelopedMarket1 <br />
DevelopedMarket2 DevelopedMarket3 EmergingAsiaPacific EmergingMarkets EnergyEquity <br />
FinancialsEquity Global Gold HealthcareEquity IndustrialsEquity <br />
InvestmentGradeCorporate Junk MaterialsEquity MunicipalBond PreferredStock <br />
RealEstate TargetMaturityDateCorporateBond TechnologyEquity TelecomEquity TotalBondMarket <br />
Treasuries UtilitiesEquity Volatility

### 績效指標
- Sharpe Raio
- Omega: 2011. Omega performance measure and portfolio insurance
- Riskness R: 2013. A global index of riskiness <br />
註：「Generalized Sharpe Ratios: 2009. Portfolio performance evaluation with generalized Sharpe ratios: Beyond the mean and variance」計算條件很多檔ETF之月報酬資料皆不滿足，因此採用傳統之Sharpe Ratio。

### 實作功能

- ETF 績效查詢：執行方式見`PerfomanceQuery`資料夾
- ETF 權重查詢：執行方式見`Portfolio`資料夾
