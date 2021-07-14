import unittest
from decimal import Decimal

from python.InvestmentPLN import InvestmentPLN
from python.InvestmentUSD import InvestmentUSD
from python.Wallet import Wallet

priceKGHM = 191.15
priceALCOA = 36.96
priceUSD = 3.80
pricePLN = 1

class WalletTest(unittest.TestCase):
    def test_wallet_init_properties(self):
        wallet_cecherz = Wallet("Kamil Cecherz")
        self.assertEqual(wallet_cecherz.owner, "Kamil Cecherz")
        self.assertEqual(wallet_cecherz.balance, 0)
        self.assertEqual(wallet_cecherz.amount_invested, 0)

    def test_calc_amount_invested(self):
        wallet_cecherz = Wallet("Kamil Cecherz")
        self.__add_investment_to_wallet(wallet_cecherz)

        wallet_cecherz.calc_amount_invested()
        self.assertEqual(wallet_cecherz.amount_invested, round(Decimal(4404.68), 2))

    def test_calc_amount_balance(self):
        wallet_cecherz = Wallet("Kamil Cecherz")
        self.__add_investment_to_wallet(wallet_cecherz)

        wallet_cecherz.calc_balance()
        self.assertEqual(wallet_cecherz.balance, round(Decimal(4018.22), 2))

    def test_money_turnover(self):
        wallet_cecherz = Wallet("Kamil Cecherz")
        self.__add_investment_to_wallet(wallet_cecherz)
        wallet_cecherz.calc_amount_invested()
        wallet_cecherz.calc_balance()
        self.assertEqual(wallet_cecherz.balance - wallet_cecherz.amount_invested, round(Decimal(-386.46), 2))

    def __add_investment_to_wallet(self, wallet_cecherz):
        KGHM = InvestmentPLN("KGHM", 10, 203.69, priceKGHM, pricePLN)
        ALCOA = InvestmentUSD("ALCOA INC", 15, 41.54, priceALCOA, priceUSD)
        wallet_cecherz.insert_investment(KGHM)
        wallet_cecherz.insert_investment(ALCOA)


if __name__ == '__main__':
    unittest.main()
