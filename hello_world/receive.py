"""
Simple receiver of rabbitMQ queue
"""
import os
import sys

import pika


def consumer_process():
    """
    Create connection with localhost standard port 5672
    Create or connect to chanel "hello"
    listen chanel and call callback function if channel will have message.
    """
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    # callback template of rabbitmq signature
    # pylint: disable-next=unused-argument
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        consumer_process()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
