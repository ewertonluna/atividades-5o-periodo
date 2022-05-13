import pika, os

def ler_msg():
# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://byblyivs:sooXqdC-0zLJq1k3zAvwRNxX7dx6CKkn@jackal.rmq.cloudamqp.com/byblyivs')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    channel.queue_declare(queue='msg-direta') # Declare a queue
    def callback(ch, method, properties, body):
        print(" [-->] Received " + str(body))

    channel.basic_consume('hello',
                        callback,
                        auto_ack=True)

    print(' [<--] Waiting for messages:')
    channel.start_consuming()
    connection.close()