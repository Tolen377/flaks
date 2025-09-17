from flask import Blueprint
math = Blueprint('math', __name__, url_prefix='/math')

@math.route('/sum/<int:n1>/<int:n2>')
def sum(n1, n2):
    return str(n1 + n2)

@math.route('/pow/<int:n1>/<int:n2>')
@math.route('/pow/<int:n1>')
def pow(n1, n2 = 2):
    return str(n1 ** n2)