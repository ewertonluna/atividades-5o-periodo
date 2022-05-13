import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://byblyivs:sooXqdC-0zLJq1k3zAvwRNxX7dx6CKkn@jackal.rmq.cloudamqp.com/byblyivs')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.exchange_declare(exchange='mensagem-em-grupo',
                         exchange_type='fanout')


result = channel.queue_declare(queue='consumidor-2')
queue_name = result.method.queue
channel.queue_bind(exchange='mensagem-em-grupo', queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()