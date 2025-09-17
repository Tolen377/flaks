from flask import Blueprint, jsonify, request
from db import db
from models.user import User

user = Blueprint("user", __name__, url_prefix="/user")

@user.route("/list")
def findAll():
    users = db.session.execute(db.select(User)).scalars().all()
    users_list = [u.toDict() for u in users]
    return jsonify(users_list)


@user.route("/insert", methods=["POST"])
def insert():
    data = request.get_json()
    newUser = User(data.get("username"), data.get("fullname"), data.get("password"))

    db.session.add(newUser)
    db.session.commit()

    return jsonify(newUser.toDict()), 201

@user.route('/find-user/<int:id>', methods=["GET"])
def findByInd(id):
    user = db.get_or_404(User, id)
    return jsonify(user.toDict()), 200

@user.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return ('Usuario con Id: "{}" borrado exitosamente').format(id)

@user.route('/update', methods=["PUT"])
def update():
    data = request.get_json()
    userId = data.get("userId")
    user = db.get_or_404(User, userId)

    user.username = data.get("username")
    user.fullname = data.get("fullname")
    user.password = data.get("password")
    db.session.commit()

    return jsonify(user.toDict()), 200
    