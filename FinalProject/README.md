## 如何選取好的 ETF

### 資料夾說明

`ETF`檔中讀取ETF清單，篩選出inception date在2015年之前的ETF，將篩選結果寫入`output.csv`。從Yahoo Finance中抓取ETF自2015年底最後一個交易日至今天的調整後收盤價（adjusted close），寫入`[directory]/XXX.csv`（XXX為某檔ETF的symbol）。

`Perfomance`

`PerfomanceQuery`

`Portfolio`

`RiskFree`

資料來源：
- [ETF](https://etfdb.com)
- [Yahoo Finance](https://www.federalreserve.gov/data/sloos.htm)

### ETF 類別
Alternatives  BroadAsia Commodity ConsumerDiscretionaryEquity ConsumerStaplesEquity
CrudeOil  Currency  DevelopedAsiaPacific  DevelopedEurope DevelopedMarket1
DevelopedMarket2  DevelopedMarket3  EmergingAsiaPacific EmergingMarkets EnergyEquity
FinancialsEquity  Global  Gold  HealthcareEquity  IndustrialsEquity
InvestmentGradeCorporate  Junk  MaterialsEquity MunicipalBond PreferredStock 
RealEstate  TargetMaturityDateCorporateBond TechnologyEquity TelecomEquity TotalBondMarket 
Treasuries UtilitiesEquity Volatility

### 實作功能
- ETF 績效查詢
```
$ python3 ETF.py [input.csv] [output.csv] [directory]
e.g.
$ python3 ETF.py DevelopedMarketsETF24.csv ETF24.csv ETF24
```
- ETF
