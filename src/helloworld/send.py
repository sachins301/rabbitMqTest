import pika

#establish connection to rabbitmq running on localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#create a queue named hello
channel.queue_declare(queue='hello')

#send a message to the default exchange
channel.basic_publish(exchange='', routing_key='hello', body='Hello World! How are you')
print("Message Sent!")

#close the rabbitmq connection
connection.close()