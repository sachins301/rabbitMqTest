import pika
import sys
import os

def main():
    #create the rabbitmq connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel = connection.channel()

    #create the queue - Just in case there is no queue in rabbitmq. If the queue with the same name exists, it wont be created again.
    channel.queue_declare(queue='hello')

    #create the callback function that will be used by the pika-rabbitmq connection
    def callback(ch, method, properties, body):
        print(f"[x] Reveived {body}")

    #pass the function to pika rmq connection
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

    print("[*] Waiting for messages. Press ctrl+c to exit.")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)