import flask
from flask import jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

json_data = {'senha_atual_normal': 0, 'senha_atual_prioridade': 0}

# rota: /api/filas/prioridade
@app.route('/api/filas/<fila>/', methods=['POST'])
def gerar_ticket(fila):
	if fila == 'normal':
		json_data['senha_atual_normal'] += 1
		return jsonify({'mensagem': 'ticket gerado na lista de normal com sucesso'})
	elif fila == 'prioridade':
		json_data['senha_atual_prioridade'] += 1
		return jsonify({'mensagem': 'ticket gerado na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})

# rota: /api/filas/
@app.route('/api/filas/', methods=['GET'])
def ver_situacao():
	return jsonify(json_data)

# rota: /api/filas/normal
@app.route('/api/filas/<fila>/', methods=['PUT'])
def chamar_ticket(fila):
	if fila == 'normal':
		json_data['senha_atual_normal'] -= 1
		return jsonify({'mensagem': 'ticket removido na lista de normal com sucesso'})
	elif fila == 'prioridade':
		json_data['senha_atual_prioridade'] -= 1
		return jsonify({'mensagem': 'ticket removido na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})

app.run()