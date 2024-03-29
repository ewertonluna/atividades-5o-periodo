import pika, os
import json

class User:
	def __init__(self, user_id: str):
		self.user_id = str(user_id)
		self._create_exchange()
		self._create_and_bind_queues(user_id)


	def write_group_message(self, message: str):
		connection = self.get_connection()
		channel = connection.channel()
		channel.basic_publish(exchange='zapzap', routing_key='group_message_key', body=message)
		connection.close()


	def write_direct_message(self, recipient: str,  message: str):
		connection = self.get_connection()
		channel = connection.channel()
		channel.basic_publish(exchange='zapzap', routing_key=recipient, body=message)
		connection.close()
	

	def read_messages(self):
		connection = self.get_connection()
		channel = connection.channel()

		def callback(ch, method, properties, body):
			print(f"Inbox Message: {body}")

		channel.basic_consume(queue=self.user_id, on_message_callback=callback, auto_ack=True)
		channel.start_consuming()


	def get_connection(self):
		settings = self._get_settings()
		url = os.environ.get('CLOUDAMQP_URL', settings['connectionUrl'])
		params = pika.URLParameters(url)
		connection = pika.BlockingConnection(params)
		return connection


	def _get_settings(self):
		json_file = open('./settings.json')
		json_object = json.load(json_file)
		json_file.close()
		return json_object
	
	def _create_exchange(self):
		connection = self.get_connection()
		channel = connection.channel()
		channel.exchange_declare(exchange='zapzap', exchange_type='direct')
		connection.close()
	

	def _create_and_bind_queues(self, queue_name: str):
		connection = self.get_connection()
		channel = connection.channel()
		result = channel.queue_declare(queue=self.user_id)
		queue_name = result.method.queue
		channel.queue_bind(exchange='zapzap', queue=queue_name, routing_key=self.user_id)
		channel.queue_bind(exchange='zapzap', queue=queue_name, routing_key='group_message_key')
		connection.close()
	

