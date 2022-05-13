# publish.py
import pika, os
def escrever_msg(msg):  

    # Access the CLODUAMQP_URL 
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://byblyivs:sooXqdC-0zLJq1k3zAvwRNxX7dx6CKkn@jackal.rmq.cloudamqp.com/byblyivs')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='msg-direta') # Declare a queue
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=msg)

    print(f"enviando a mensagem {msg}'")
    connection.close()