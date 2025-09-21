from flask import Flask
from routes import math,page,products,users,order
from db import db

def create_app():
    app = Flask(__name__)
    app.register_blueprint(math.math)
    app.register_blueprint(page.page)
    app.register_blueprint(products.products)
    app.register_blueprint(users.user)
    app.register_blueprint(order.order)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:tmao180176@localhost/learn_flask"
    db.init_app(app)
    return app