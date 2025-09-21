from datetime import datetime
from sqlalchemy import inspect
from db import db


class User(db.Model):
    userId = db.Column("user_id", db.Integer, primary_key=True)
    username = db.Column(db.String(10), nullable=False, unique=True)
    fullname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    creationDate = db.Column("creation_date", db.DateTime, default=datetime.now)

    orders = db.relationship('Order', back_populates="user")
    def __init__(self, username, fullname, password):
        self.username = username
        self.fullname = fullname
        self.password = password

    def toDict(self):
        return {
            "fullname": self.fullname,
            "username": self.username,
            "orders": [order.toDict() for order in self.orders]
        }

