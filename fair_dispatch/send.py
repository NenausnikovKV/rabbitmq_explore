"""Simple publisher for rabbitmq"""

import pika


def publisher_process():
    """
    Create connection with localhost standard port 5672
    Create or connect to chanel "hello"
    Publish to channel message string
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    publisher_process()
