import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='workqueue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    #Simulating a task
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

#fair dispatch - 1 task/message at a time per worker
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='workqueue', on_message_callback=callback)

channel.start_consuming()