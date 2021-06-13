class Investments(object):
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)


    # def __init__(self, name, kind, purchase_price_unit, purchase_date, actual_price_unit):
    #     self.name = name
    #     self.kind = kind
    #     self.purchase_price_unit = purchase_price_unit
    #     self.purchase_date = purchase_date
    #     self.actual_price_unit = actual_price_unit