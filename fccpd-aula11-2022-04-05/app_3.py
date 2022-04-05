
import flask
from flask import request, jsonify 
from flask import Blueprint

from fila_api import FilaAPI

fila_view = FilaAPI.as_view('fila_api')

bp = Blueprint('blueprint', __name__, url_prefix='/api/filas')
bp.add_url_rule('/', view_func=fila_view, methods=['GET'])
bp.add_url_rule('/<fila>/', view_func=fila_view, methods=['PUT', 'POST'])

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.register_blueprint(bp)
app.run()
