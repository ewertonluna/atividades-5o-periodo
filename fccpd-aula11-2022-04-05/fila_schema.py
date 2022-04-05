from marshmallow import Schema, fields

# json_data = {'senha_atual_normal': 0, 'senha_atual_prioridade': 0}

class FilaSchema(Schema):
	senha_atual_normal = fields.Int()	
	senha_atual_prioridade = fields.Int()