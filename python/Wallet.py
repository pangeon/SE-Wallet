from decimal import Decimal

from python.InvestmentPLN import InvestmentPLN
from python.InvestmentUSD import InvestmentUSD


class Wallet:
    def __init__(self, owner):
        self._owner = str(owner)
        self._investments = []
        self._balance = Decimal(0)
        self._amount_invested = Decimal(0)

    def __str__(self) -> str:
        return "owner: {}, investments: {}, balance = {}, amount_invested = {}" \
            .format(self._owner, self._investments, self._balance, self._amount_invested)

    def __iter__(self):
        return iter(self._investments)

    def add_investment(self, name, amount, buy_price, actual_price, currency_price, currency_symbol):
        global investment
        if currency_symbol == "PLN":
            investment = InvestmentPLN(name, amount, buy_price, actual_price, currency_price)
            investment.purchase_value = amount * buy_price * currency_price
            investment.share_value = amount * actual_price * currency_price
        elif currency_symbol == "USD":
            investment = InvestmentUSD(name, amount, buy_price, actual_price, currency_price)
            investment.purchase_value = amount * buy_price * currency_price
            investment.share_value = amount * actual_price * currency_price

        self._investments.append(investment)

    def insert_investment(self, investment):
        if isinstance(investment, InvestmentPLN):
            investment.purchase_value = investment.amount * investment.buy_price * investment.pln_price
            investment.share_value = investment.amount * investment.actual_price * investment.pln_price
            self._investments.append(investment)
        elif isinstance(investment, InvestmentUSD):
            investment.purchase_value = investment.amount * investment.buy_price * investment.usd_price
            investment.share_value = investment.amount * investment.actual_price * investment.usd_price
            self._investments.append(investment)
        else:
            raise Exception("Incompatible type")

    def money_turnover(self):
        return round(self._balance - self._amount_invested, 2)

    @property
    def investments(self):
        return self._investments

    @investments.setter
    def investments(self, value):
        self._investments = value

    @property
    def balance(self):
        investments = self._investments
        for investment in investments:
            self._balance += Decimal(investment.share_value)

        return round(self._balance, 2)

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def amount_invested(self):
        investments = self._investments
        for investment in investments:
            self._amount_invested += Decimal(investment.purchase_value)

        return round(self._amount_invested, 2)

    @amount_invested.setter
    def amount_invested(self, value):
        self._amount_invested = value
