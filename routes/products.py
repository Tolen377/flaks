from flask import Blueprint
products = Blueprint('products', __name__, url_prefix='/products')

@products.route('/list')
def productsList():
    return 'Lista de productos'

@products.route('/insert')
def insertProduct():
    return 'success'