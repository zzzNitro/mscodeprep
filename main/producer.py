import pika, json

params = pika.URLParameters('amqps://vvuezdxt:1raZjgjaQDUPcVvECMPdjerQ08mC2pVk@snake.rmq2.cloudamqp.com/vvuezdxt')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
