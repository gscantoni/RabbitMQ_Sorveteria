import pika
import time

url = "amqps://adfkdmpq:75isAYvZvIBHeICZbBlvDbdBHliFKiIy@prawn.rmq.cloudamqp.com/adfkdmpq"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='pedidos_sorvete')

def callback(ch, method, properties, body):
    print(f"Pedido recebido: {body.decode()}")
    time.sleep(2)  # Simula o tempo de preparo do sorvete
    print(f"Pedido processado: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='pedidos_sorvete', on_message_callback=callback)

print('Aguardando pedidos...')
channel.start_consuming()
