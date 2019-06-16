## 功能實作二

### 計算最佳權重
查詢33個ETF類別中，任選其中的類別，計算最適配置權重，寫入`weight.csv`。

### ETF 類別
Alternatives BroadAsia Commodity ConsumerDiscretionaryEquity ConsumerStaplesEquity <br />
CrudeOil Currency DevelopedAsiaPacific DevelopedEurope DevelopedMarket1 <br />
DevelopedMarket2 DevelopedMarket3 EmergingAsiaPacific EmergingMarkets EnergyEquity <br />
FinancialsEquity Global Gold HealthcareEquity IndustrialsEquity <br />
InvestmentGradeCorporate Junk MaterialsEquity MunicipalBond PreferredStock <br />
RealEstate TargetMaturityDateCorporateBond TechnologyEquity TelecomEquity TotalBondMarket <br />
Treasuries UtilitiesEquity Volatility

### 執行方法
- 在33個ETF類別中，將RisknessR排前25%的ETF等權重組成33支類別ETF標的，並計算將33個類別ETF標的月報酬率寫入`month.csv`。
```
$ pytpython3 select_etf
```
- 績效查詢
```
$ pytpython3 portfolio.py [categories]
e.g.
$ pytpython3 portfolio.py Alternatives BroadAsia Commodity ConsumerDiscretionaryEquity 
  ConsumerStaplesEquity CrudeOil Currency DevelopedAsiaPacific DevelopedEurope 
  DevelopedMarket1 DevelopedMarket2 DevelopedMarket3 EmergingAsiaPacific EmergingMarkets 
  EnergyEquity FinancialsEquity Global Gold HealthcareEquity IndustrialsEquity 
  InvestmentGradeCorporate Junk MaterialsEquity MunicipalBond PreferredStock RealEstate 
  TargetMaturityDateCorporateBond TechnologyEquity TelecomEquity TotalBondMarket 
  Treasuries UtilitiesEquity Volatility
```
