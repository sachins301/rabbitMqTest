import sys
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
#durable is set to true to persist messages in queue in case rabbitmq crash
channel.queue_declare(queue='workqueue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='workqueue', body=message,
                      properties=pika.BasicProperties(
                          delivery_mode = pika.DeliveryMode.Persistent
                      ))
print(f"[x] Sent {message}")
connection.close()