from datetime import datetime
from sqlalchemy import inspect
from db import db


class Order(db.Model):
    __tablename__ = "orders"

    orderId = db.Column("order_id", db.Integer, primary_key=True)
    items = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    contactNumber = db.Column("contact_number", db.Integer, nullable=False)
    creationDate = db.Column("creation_date", db.DateTime, default=datetime.now)

    userId = db.Column("user_id", db.Integer, db.ForeignKey('user.user_id'), nullable = False)
    user = db.relationship('User', back_populates="orders", uselist=False)

    def __init__(self,items, address, contactNumber):
        self.items = items
        self.address = address
        self.contactNumber = contactNumber

    def toDict(self):
        return {
            "orderId": self.orderId,
            "items": self.items,
            "address": self.address,
            "contactNumber": self.contactNumber,
        }

