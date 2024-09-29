import pika

url = "amqps://adfkdmpq:75isAYvZvIBHeICZbBlvDbdBHliFKiIy@prawn.rmq.cloudamqp.com/adfkdmpq"
params = pika.URLParameters(url)

# Conexão com RabbitMQ
print("Conectando ao RabbitMQ...")
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Declarar o exchange de novos sabores
print("Declarando o exchange 'novos_sabores'...")
channel.exchange_declare(exchange='novos_sabores', exchange_type='fanout')

# Criar uma fila temporária para o subscriber
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
print(f"Fila temporária criada: {queue_name}")

# Vincular a fila ao exchange
channel.queue_bind(exchange='novos_sabores', queue=queue_name)
print(f"Fila vinculada ao exchange 'novos_sabores'")

# Callback para processar mensagens
def callback(ch, method, properties, body):
    print(f"Novo sabor recebido: {body.decode()}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print('Aguardando novos sabores...')
channel.start_consuming()
