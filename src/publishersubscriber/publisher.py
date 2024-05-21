import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#exchange type set to fan out. Send message to all consumers.
channel.exchange_declare(exchange="logsexchange", exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

#leaving routing blanks sets a random queue name
channel.basic_publish(exchange='logsexchange', routing_key='', body=message)

print(f"[x] Sent {message}")
connection.close()