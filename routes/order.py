from flask import Blueprint, jsonify, request
from db import db
from models.order import Order
from models.user import User

order = Blueprint("order", __name__, url_prefix="/order")

@order.route("/insert", methods=["POST"])
def insert():
    data = request.get_json()
    user = db.get_or_404(User, data.get("userId"))
    newOrder = Order(data.get("items"), data.get("address"), data.get("contactNumber"))
    newOrder.user = user
    db.session.add(newOrder)
    db.session.commit()
    return jsonify(newOrder.toDict()), 201  


@order.route("/list",  methods=["GET"])
def findAll():    
    orders = db.session.execute(db.select(Order)).scalars().all()
    orders_list = [o.toDict() for o in orders]
    return jsonify(orders_list)

@order.route("/<int:orderId>", methods=["GET"])
def findOrder(orderId):    
    order = db.get_or_404(Order, orderId)
    return jsonify(order.toDict()), 200