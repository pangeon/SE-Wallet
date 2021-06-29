from python.Investments import Investments

class InvestmentsFunds(Investments):
    def __init__(self, iterable=(), **kwargs):
        super().__init__(iterable, **kwargs)
