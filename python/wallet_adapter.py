from flask import session
from python.Wallet import Wallet
import logging

priceKGHM = 191.15
priceALCOA = 36.96
priceUSD = 3.80
pricePLN = 1

wallet = None
update = True


def create_wallet(owner):
    global wallet
    wallet = Wallet(owner)
    session['owner'] = owner
    logging.debug(f"wallet_adapter :: Wallet owner: {wallet.owner}")
    return wallet


def investments():
    global wallet

    if wallet is not None:
        return wallet.investments
    else:
        return []


def summary():
    global wallet
    global update

    if wallet is not None:
        if update is True:
            wallet.calc_amount_invested()
            wallet.calc_balance()
            update = False

        logging.debug(f"wallet_adapter :: Wallet summary: "
        f"{(session['owner'], wallet.amount_invested, wallet.balance, wallet.money_turnover())}")
        logging.debug(f"update: {update} ")
        return str(session['owner']), \
               str(wallet.amount_invested) + " PLN", \
               str(wallet.balance) + " PLN", \
               str(wallet.money_turnover()) + " PLN"
    else:
        return []
