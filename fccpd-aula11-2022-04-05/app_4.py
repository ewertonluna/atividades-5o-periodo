import flask
from flask import request, jsonify 
from fila_schema import FilaSchema

fila = {'senha_atual_normal': 0, 'senha_atual_prioridade': 0}
fila_schema = FilaSchema()
result = fila_schema.dump(fila)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# rota: /api/filas/prioridade
@app.route('/api/filas/<fila>/', methods=['POST'])
def gerar_ticket(fila):
	if fila == 'normal':
		result.senha_atual_normal += 1	
		return jsonify({'mensagem': 'ticket gerado na lista de normal com sucesso'})
	elif fila == 'prioridade':
		result.senha_atual_normal += 1	
		return jsonify({'mensagem': 'ticket gerado na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})


# rota: /api/filas/
@app.route('/api/filas/', methods=['GET'])
def ver_situacao():
	return jsonify(result)


# rota: /api/filas/normal
@app.route('/api/filas/<fila>/', methods=['PUT'])
def chamar_ticket(fila):
	if fila == 'normal':
		result['senha_atual_normal'] -= 1	
		return jsonify({'mensagem': 'ticket removido na lista de normal com sucesso'})
	elif fila == 'prioridade':
		result['senha_atual_normal'] -= 1	
		return jsonify({'mensagem': 'ticket removido na lista de prioridade com sucesso'})
	return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})


app.run()
