from flask import Blueprint, render_template, jsonify, request

from python import wallet_adapter

get_data = Blueprint('get_data', __name__)


@get_data.route("/")
def wallet_state():
    return render_template("summary.html", wallet=wallet_adapter.summary())


@get_data.route("/login-form", methods=['GET'])
def login_form():
    placeholders = {"username": "Enter your username", "password": "Enter your password"}
    return render_template('login_form.html', hints=placeholders)


@get_data.route("/login", methods=['POST'])
def login():
    if request.form["login"] == "cecherz" and request.form["password"] == "secret":
        return jsonify("Login success")
    else:
        return jsonify("Access denied !")


@get_data.route("/investments")
def investments_list():
    return render_template("investments.html", investments=wallet_adapter.investments())
