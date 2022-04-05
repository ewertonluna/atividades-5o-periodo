import flask
from flask import request, jsonify 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/filas')
def show(fila):
	return jsonify({'fila': fila})

app.run()