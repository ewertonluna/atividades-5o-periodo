import pika, os
import json

class User:
	def __init__(self, use_id: str):
		self.user_id = str(use_id)
		self.user_queue = str(use_id)
	
	def write_direct_message(self, recipient:str, message:str):
		settings = self._get_settings()
		url = os.environ.get('CLOUDAMQP_URL', settings['connectionUrl'])
		params = pika.URLParameters(url)
		connection = pika.BlockingConnection(params)
		channel = connection.channel()
		channel.exchange_declare(exchange='direct_message', exchange_type='direct')
		channel.queue_declare(queue=recipient)
		channel.basic_publish(exchange='direct_message', routing_key=recipient, body=message)
		connection.close()

	def write_group_message(self, message:str):
		settings = self._get_settings()
		url = os.environ.get('CLOUDAMQP_URL', settings['connectionUrl'])
		params = pika.URLParameters(url)
		connection = pika.BlockingConnection(params)
		channel = connection.channel()
		channel.exchange_declare(exchange='group_message', exchange_type='fanout')
		channel.basic_publish(exchange='group_message', routing_key='', body=message)
		connection.close()

	def read_direct_messages(self):
		settings = self._get_settings()
		url = os.environ.get('CLOUDAMQP_URL', settings['connectionUrl'])
		params = pika.URLParameters(url)
		connection = pika.BlockingConnection(params)
		channel = connection.channel()
		channel.exchange_declare(exchange='direct_message', exchange_type='direct')
		result = channel.queue_declare(queue=self.user_queue)
		queue_name = result.method.queue
		channel.queue_bind(exchange='direct_message', queue=queue_name, routing_key=self.user_queue)

		def callback(ch, method, properties, body):
			print(f"Received Message: {body}")

		channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
		channel.start_consuming()
	

	def read_group_messages(self):
		settings = self._get_settings()
		url = os.environ.get('CLOUDAMQP_URL', settings['connectionUrl'])
		params = pika.URLParameters(url)
		connection = pika.BlockingConnection(params)
		channel = connection.channel()
		channel.exchange_declare(exchange='group_message', exchange_type='fanout')
		result = channel.queue_declare(queue=self.user_queue)
		queue_name = result.method.queue
		channel.queue_bind(exchange='group_message', queue=queue_name, routing_key=self.user_queue)

		def callback(ch, method, properties, body):
			print(f"Received Message: {body}")

		channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
		channel.start_consuming()

	def _get_settings(self):
		json_file = open('./settings.json')
		json_object = json.load(json_file)
		json_file.close()
		return json_object


user_1 = User('1')
user_2 = User('2')
# user_1.write_direct_message('1', 'Enviando do usuario 1 para o usuário 1')
# user_1.write_direct_message('1', 'Tudo bem?')
# user_1.write_group_message('Bom dia, grupo!')
# user_2.read_group_messages()
# user_1.read_group_messages()
