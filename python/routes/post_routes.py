import logging
from decimal import Decimal

from flask import Blueprint, request, render_template, url_for
from werkzeug.utils import redirect

from python import wallet_adapter

post_data = Blueprint('post_data', __name__)


@post_data.route("/add_owner", methods=['POST', 'GET'])
def add_owner():
    if request.method == "POST":
        global wallet

        owner = str(request.form["owner"])
        wallet = wallet_adapter.create_wallet(owner)
        return redirect(url_for('get_data.investments_list'))
    else:
        return render_template("create_wallet_form.html")


@post_data.route("/add_investment", methods=['POST', 'GET'])
def add_investment():
    if request.method == 'POST':
        global wallet
        global update

        name = str(request.form["name"])
        amount = int(request.form["amount"])
        buy_price = Decimal(request.form["buy_price"])
        actual_price = Decimal(request.form["actual_price"])
        currency_price = Decimal(request.form["currency_price"])
        currency_symbol = str(request.form["currency_symbol"])

        wallet.add_investment(name, amount, buy_price, actual_price, currency_price, currency_symbol)

        logging.debug(f"post_routes :: New investment in Wallet: "
        f"{name, amount, buy_price, actual_price, currency_price, currency_symbol}")

        wallet_adapter.update = True
        return redirect(url_for('get_data.investments_list'))
    else:
        return render_template("add_investment_form.html")
