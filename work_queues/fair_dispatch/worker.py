"""
Simple receiver of rabbitMQ queue
Fair dispatch
"""
import os
import sys
import time

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
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello', on_message_callback=callback)
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
