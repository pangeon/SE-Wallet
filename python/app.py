from decimal import Decimal

from flask import Flask, request, jsonify, render_template, url_for, session
from werkzeug.utils import redirect

from python.Wallet import Wallet

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
        return str(session['owner']), \
               str(wallet.amount_invested) + " PLN", \
               str(wallet.balance) + " PLN", \
               str(wallet.money_turnover()) + " PLN"
    else:
        return []

app = Flask(__name__)

@app.route("/")
def wallet_state():
    return render_template("summary.html", wallet=summary())


@app.route("/add_owner", methods=['POST', 'GET'])
def add_owner():
    if request.method == "POST":
        global wallet

        owner = str(request.form["owner"])
        wallet = create_wallet(owner)
        return redirect(url_for('investments_list'))
    else:
        return render_template("create_wallet_form.html")


@app.route("/add_investment", methods=['POST', 'GET'])
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
        update = True
        return redirect(url_for('investments_list'))
    else:
        return render_template("add_investment_form.html")


@app.route("/investments")
def investments_list():
    return render_template("investments.html", investments=investments())


@app.route("/login", methods=['POST'])
def login():
    if request.form["login"] == "cecherz" and request.form["password"] == "secret":
        return jsonify("Login success")
    else:
        return jsonify("Access denied !")


@app.route("/login-form", methods=['GET'])
def login_form():
    placeholders = {"username": "Enter your username", "password": "Enter your password"}
    return render_template('login_form.html', hints=placeholders)


if __name__ == '__main__':
    app.secret_key = "secret value"
    app.run(debug=True)
