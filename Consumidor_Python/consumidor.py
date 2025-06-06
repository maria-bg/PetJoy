import pika  # type: ignore

# Conexão com o RabbitMQ pelo CloudAMQP
url = 'amqps://pzfafvhx:o5wRgx64SsXd1RI50ZcXxKeT1QdAFi0P@jackal.rmq.cloudamqp.com/pzfafvhx'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# Setando o Topic Exchange
exchange_name = 'pet_joy_hotelzinho'
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

# ------------------------------------------------------------------------------------------------


def callback(ch, method, properties, body):
    print(f"\n{body.decode()}")
    print("\nAguarde novas atualizações ou escolha outra opção pressionando Ctrl + C.")


def menu_cons(channel):
    print("\nDeseja ouvir sobre alguma categoria em específico?")
    print("1) Atualizações Gerais")
    print("2) Saúde")
    print("3) Limpeza")
    print("4) Diversão")
    print("5) Feedback")
    print("6) Alimentação")
    print("0) Voltar para o Menu")

    try:
        opcao = int(input().strip())
    except ValueError:
        print("\nOpção inválida! Tente novamente.")
        return menu_cons(channel)

    routing_keys = {
        1: "#",
        2: "saude",
        3: "limpeza",
        4: "diversao",
        5: "feedback",
        6: "alimentacao",
    }

    if opcao == 0:
        print("\nVoltando ao menu principal...")
        return False
    elif opcao in routing_keys:
        routing_key = routing_keys[opcao]
    else:
        print("\nOpção inválida! Tente novamente.")
        return menu_cons(channel)

    queue = channel.queue_declare('', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue,
                       routing_key=routing_key)

    print("\nAguardando mensagens do PetJoy Hotel...")

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True)

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário. Encerrando...")


# Ações do Consumidor:
print("Bem-vindo(a) ao canal de comunicação do PetJoy!")
print("Você está antenado nas informações gerais do nosso hotelzinho!")

while True:
    continuar = menu_cons(channel)
    if not continuar:
        break
