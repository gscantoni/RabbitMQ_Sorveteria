import pika
import time

url = "amqps://adfkdmpq:75isAYvZvIBHeICZbBlvDbdBHliFKiIy@prawn.rmq.cloudamqp.com/adfkdmpq"
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(exchange='novos_sabores', exchange_type='fanout')

def anunciar_sabor(sabor):
    channel.basic_publish(exchange='novos_sabores', routing_key='', body=sabor)
    print(f"Anunciado novo sabor: {sabor}")

# Simula o anúncio contínuo de novos sabores
while True:
    sabor = input("Digite o novo sabor (ou 'sair' para encerrar): ")
    if sabor.lower() == 'sair':
        break
    anunciar_sabor(sabor)
    time.sleep(2)  # Simula intervalo entre anúncios

connection.close()
