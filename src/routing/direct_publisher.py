import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#set exchange type as direct
channel.exchange_declare(exchange='direct_exchange', exchange_type='direct')

#routing key of the publisher
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange='direct_exchange', routing_key=severity, body=message)

print(f" [x] Sent {severity}:{message}")
connection.close()