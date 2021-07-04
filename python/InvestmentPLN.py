from decimal import Decimal

from python.Investment import Investment


class InvestmentPLN(Investment):
    def __init__(self, name, amount, buy_price, actual_price, pln_price):
        super().__init__(name, amount, buy_price, actual_price)
        self._pln_price = Decimal(pln_price)

    def __str__(self) -> str:
        return super().__str__() + ", PLN price = {}".format(round(self._pln_price, 2))

    @property
    def pln_price(self):
        return self._pln_price

    @pln_price.setter
    def pln_price(self, value):
        self._pln_price = value
