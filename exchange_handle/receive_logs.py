"""receive for broadcast exchange 'logs'"""
import pika

def receive():
    """receive for 'logs' exchange"""
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # declare random name queue for one connection
    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue
    # bind queue to given exchange
    channel.queue_bind(exchange='logs', queue=queue_name)
    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(_ch, _method, _properties, body):
        """callback for message receiving"""
        print(f" [x] {body}")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    receive()
