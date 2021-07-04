from python.InvestmentPLN import InvestmentPLN
from python.InvestmentUSD import InvestmentUSD
from python.Wallet import Wallet

priceKGHM = 191.15
priceALCOA = 36.96
priceUSD = 3.80
pricePLN = 1


def print_wallet(wallet):
    for investment in wallet:
        print(investment)

    print("Invested money: {}".format(wallet.amount_invested))
    print("The value of your stocks: {}".format(wallet.balance))
    print("Profit on turnover: {}".format(wallet.money_turnover()))


if __name__ == '__main__':
    wallet_cecherz = Wallet("Kamil Cecherz")
    wallet_agnieszka = Wallet("Agnieszka Lasota")

    KGHM = InvestmentPLN("KGHM", 10, 203.69, priceKGHM, pricePLN)
    ALCOA = InvestmentUSD("ALCOA INC", 15, 41.54, priceALCOA, priceUSD)

    wallet_cecherz.insert_investment(KGHM)
    wallet_cecherz.insert_investment(ALCOA)

    wallet_agnieszka.add_investment("KGHM", 10, 203.69, priceKGHM, pricePLN, "PLN")
    wallet_agnieszka.add_investment("ALCOA INC", 15, 41.54, priceALCOA, priceUSD, "USD")

    print_wallet(wallet_cecherz)
    print_wallet(wallet_agnieszka)

