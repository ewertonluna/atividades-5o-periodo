import flask
from flask import request, jsonify 
from flask import Blueprint

bp = Blueprint('blueprint', __name__, url_prefix='/api/filas')
json_data = {'senha_atual_normal': 0, 'senha_atual_prioridade': 0}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# rota: /api/filas/prioridade
@bp.route('/<fila>/', methods=['POST'])
def gerar_ticket(fila):
	if fila == 'normal':
		json_data['senha_atual_normal'] += 1
		return jsonify({'mensagem': 'ticket gerado na lista de normal com sucesso'})
	elif fila == 'prioridade':
		json_data['senha_atual_prioridade'] += 1
		return jsonify({'mensagem': 'ticket gerado na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})

# rota: /api/filas/
@bp.route('/', methods=['GET'])
def ver_situacao():
	return jsonify(json_data)

# rota: /api/filas/normal
@bp.route('/<fila>/', methods=['PUT'])
def chamar_ticket(fila):
	if fila == 'normal':
		json_data['senha_atual_normal'] -= 1
		return jsonify({'mensagem': 'ticket removido na lista de normal com sucesso'})
	elif fila == 'prioridade':
		json_data['senha_atual_prioridade'] -= 1
		return jsonify({'mensagem': 'ticket removido na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})

app.register_blueprint(bp)
app.run()
