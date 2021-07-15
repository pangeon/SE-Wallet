import logging

from flask import Flask
from python.routes import get_routes, post_routes


logging.basicConfig(filename="logs/application.log", level=logging.DEBUG)

app = Flask(__name__)
app.register_blueprint(get_routes.get_data)
app.register_blueprint(post_routes.post_data)

if __name__ == '__main__':
    app.secret_key = "secret value"
    app.run(debug=True)
