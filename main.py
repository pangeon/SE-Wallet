from model.Owner import Owner
from model.Wallet import Wallet
from model.StockMarketShares import StockMarketShares
from model.InvestmentsFunds import InvestmentsFunds

print('Welcome to SE-Wallet')
owner_1 = Owner('Kamil', 'Cecherz', 'kamil.cecherz@gmail.com', '15-02-1986')
stock_market_shares = StockMarketShares({'amount': '90'})
investments_funds = InvestmentsFunds({'ABC': '50'})
wallet_1 = Wallet(owner_1, 3500, stock_market_shares, investments_funds)


print(owner_1)
print(wallet_1)
print(int(stock_market_shares.amount) * 5)


