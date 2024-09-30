"""Durable publisher for rabbitmq"""
import sys

import pika


def publisher_process():
    """
    Create connection with localhost standard port 5672
    Create or connect to chanel "hello"
    Publish to channel message string

    """
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message,
                          properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent),
                          )
    print(f" [x] Sent {message}'")
    connection.close()


if __name__ == '__main__':
    publisher_process()
