import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logsexchange', exchange_type='fanout')

#setting exclusive = true closes the queue once the consumer connection is closed
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

#bind the queues with the exchanges
channel.queue_bind(exchange='logsexchange', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(f" [x] {body}")

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()