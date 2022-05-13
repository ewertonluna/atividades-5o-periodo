import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://byblyivs:sooXqdC-0zLJq1k3zAvwRNxX7dx6CKkn@jackal.rmq.cloudamqp.com/byblyivs')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.exchange_declare(exchange='mensagem-em-grupo',
                         exchange_type='fanout')

channel.basic_publish(exchange='mensagem-em-grupo',
                      routing_key='',
                      body="Oi, pessoal")

result_1 = channel.queue_declare(queue='consumidor-1')
result_2 = channel.queue_declare(queue='consumidor-2')

channel.queue_bind(exchange='mensagem-em-grupo',
                   queue=result_1.method.queue)

channel.queue_bind(exchange='mensagem-em-grupo',
                   queue=result_2.method.queue)

connection.close()	