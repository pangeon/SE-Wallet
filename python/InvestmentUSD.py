from decimal import Decimal

from python.Investment import Investment


class InvestmentUSD(Investment):
    def __init__(self, name, amount, buy_price, actual_price, usd_price):
        super().__init__(name, amount, buy_price, actual_price)
        self._usd_price = Decimal(usd_price)

    def __str__(self) -> str:
        return super().__str__() + ", USD price = {}".format(round(self._usd_price, 2))

    @property
    def usd_price(self):
        return self._usd_price

    @usd_price.setter
    def usd_price(self, value):
        self._usd_price = value


