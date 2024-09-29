import pika
import time

url = "amqps://adfkdmpq:75isAYvZvIBHeICZbBlvDbdBHliFKiIy@prawn.rmq.cloudamqp.com/adfkdmpq"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='pedidos_sorvete')

def enviar_pedido(pedido):
    channel.basic_publish(exchange='', routing_key='pedidos_sorvete', body=pedido)
    print(f"Pedido enviado: {pedido}")

while True:
    pedido = input("Digite o pedido de sorvete (ou 'sair' para encerrar): ")
    if pedido.lower() == 'sair':
        break
    enviar_pedido(pedido)
    time.sleep(1)  

connection.close()
