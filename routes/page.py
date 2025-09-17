from flask import Blueprint
page = Blueprint('page', __name__)

@page.route('/home')
def home():
    return 'Bienvenidos'

@page.route('/about-us')
def aboutUs():
    return 'Acerca de nosotros'