from flask import Flask
from python.InvestmentPLN import InvestmentPLN
from python.InvestmentUSD import InvestmentUSD
from python.Wallet import Wallet

priceKGHM = 191.15
priceALCOA = 36.96
priceUSD = 3.80
pricePLN = 1


def investments():
    wallet_cecherz = Wallet("Kamil Cecherz")

    wallet_cecherz.add_investment("KGHM", 10, 203.69, priceKGHM, pricePLN, "PLN")
    wallet_cecherz.add_investment("ALCOA INC", 15, 41.54, priceALCOA, priceUSD, "USD")

    return wallet_cecherz.investments


def wallet():
    wallet_cecherz = Wallet("Kamil Cecherz")

    KGHM = InvestmentPLN("KGHM", 10, 203.69, priceKGHM, pricePLN)
    ALCOA = InvestmentUSD("ALCOA INC", 15, 41.54, priceALCOA, priceUSD)

    wallet_cecherz.insert_investment(KGHM)
    wallet_cecherz.insert_investment(ALCOA)

    return str(wallet_cecherz.amount_invested), str(wallet_cecherz.balance), str(wallet_cecherz.money_turnover())


app = Flask(__name__)


@app.route("/")
def wallet_state():
    return "Invested money: {} PLN" \
           "<br /> The value of your stocks: {} PLN" \
           "<br /><br /> Profit on turnover: {} PLN" \
        .format(wallet()[0], wallet()[1], wallet()[2])


@app.route("/investments")
def investments_list():
    result = ""
    for item in investments():
        result += str(item) + "<br />"
    return result


if __name__ == '__main__':
    app.run(debug=True)
