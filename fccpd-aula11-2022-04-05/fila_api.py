from flask.views import MethodView
from flask import jsonify, request


json_data = {'senha_atual_normal': 0, 'senha_atual_prioridade': 0}
class FilaAPI(MethodView):
	
	def get(self):
		return jsonify(json_data)
	
	def post(self, fila):
		if fila == 'normal':
			json_data['senha_atual_normal'] += 1
			return jsonify({'mensagem': 'ticket gerado na lista de normal com sucesso'})
		elif fila == 'prioridade':
			json_data['senha_atual_prioridade'] += 1
			return jsonify({'mensagem': 'ticket gerado na lista de prioridade com sucesso'})
		return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})

	def put(self, fila):
		if fila == 'normal':
			json_data['senha_atual_normal'] -= 1
			return jsonify({'mensagem': 'ticket removido na lista de normal com sucesso'})
		elif fila == 'prioridade':
			json_data['senha_atual_prioridade'] -= 1
			return jsonify({'mensagem': 'ticket removido na lista de prioridade com sucesso'})
		return jsonify({'mensagem': 'a rota tem que ser /api/filas/normal ou /api/filas/prioridade'})