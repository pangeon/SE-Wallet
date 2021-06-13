# SE-Wallet
Stock Exchange Wallet: stocks, investment funds

## Wallet view

```
VALUE OF FINANCIAL INSTRUMENTS:

| name  |   purchase price    | actual price | varation |
|-------|---------------------|--------------|----------|
| KGHM  |       200.00        |    201.00    |  +0.5%   |
|-------|---------------------|--------------|----------|
| PGE   |       30.00         |    28.00     |  -6.66%  |
|-------|---------------------|--------------|----------|
| ALCOA |       40.00         |    45.00     |  +12.5%  |

SUMMARY:
_________________________________________________________
| SMS   |       230.00        |    230.00    |  0%      |
|-------|---------------------|--------------|----------|

_________________________________________________________
| SI    |       40.00         |    45.00     |  +12.5%  |
|-------|---------------------|--------------|----------|

_________________________________________________________
| SUM   |       270.00        |    275.00    |  +1.85%  |
|-------|---------------------|--------------|----------|
```
## Data model

### Wallet
- properties:
    - account balance
    - value of financial instruments:
        - money in SMS:

            ```[(SMS[name_1].amount * SMS[name_1].actual_price) + (SMS[name_2].amount * SMS[name_2].actual_price)]```
 
        - money in SI:
        
            ```[(SI[name_1].amount * SI[name_1].actual_price) + (SI[name_2].amount * SI[name_2].actual_price)]```

    - SMS units: 
    
        ```{"name_1"="amount", "name_2"="amount" ... }```

    - SI units:

        ```{"name_1"="amount", "name_2"="amount" ... }```
### Owner
- properties:
    - name
    - surname
    - e-mail
    - birth date

### FinancialInstrument
- StockMarketShares (SMS)
    - properies:
        - name (unique)
        - kind
        - purchase price of unit
        - purchase date
        - actual price of unit
        - variation
- InvestmentFunds (IF)
    - properies:
        - name (unique)
        - kind
        - purchase price of unit
        - purchase date
        - actual price of unit
        - variation    