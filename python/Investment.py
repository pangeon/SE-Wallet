from decimal import Decimal


class Investment:
    def __init__(self, name, amount, buy_price, actual_price):
        self._name = str(name)
        if amount <= 0 or actual_price <= 0:
            raise Exception("Negative value of amount investments or price.")
        else:
            self._amount = Decimal(amount)
            self._buy_price = Decimal(buy_price)
            self._actual_price = Decimal(actual_price)
            self._purchase_value = 0
            self._share_value = 0


    def __str__(self) -> str:
        return "name: {}, amount = {}, " \
               "buy price = {}, actual price = {}, " \
               "purchase_value {} PLN, share value = {} PLN"\
            .format(
                self._name,
                self.amount,
                round(self._buy_price, 2),
                round(self._actual_price, 2),
                round(self._purchase_value, 2),
                round(self._share_value, 2)
        )

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def buy_price(self):
        return self._buy_price

    @buy_price.setter
    def buy_price(self, value):
        self._buy_price = value

    @property
    def actual_price(self):
        return self._actual_price

    @actual_price.setter
    def actual_price(self, value):
        self._actual_price = value

    @property
    def purchase_value(self):
        return self._purchase_value

    @purchase_value.setter
    def purchase_value(self, value):
        self._purchase_value = value

    @property
    def share_value(self):
        return self._share_value

    @share_value.setter
    def share_value(self, value):
        self._share_value = value


