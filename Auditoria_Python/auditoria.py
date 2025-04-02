import pika  # type: ignore

url = 'amqps://pzfafvhx:o5wRgx64SsXd1RI50ZcXxKeT1QdAFi0P@jackal.rmq.cloudamqp.com/pzfafvhx'
params = pika.URLParameters(url)

connection = pika.BlockingConnection(params)
channel = connection.channel()

exchange_name = 'pet_joy_hotelzinho'
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

queue = channel.queue_declare('', exclusive=True).method.queue
channel.queue_bind(exchange=exchange_name, queue=queue, routing_key='#')

print("Backend de Auditoria - Aguardando todas as mensagens...\n")


def callback(ch, method, properties, body):
    print(f"[AUDITORIA] {body.decode()}")


channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
channel.start_consuming()
