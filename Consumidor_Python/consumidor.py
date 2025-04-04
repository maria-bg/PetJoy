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
    # Exibe a mensagem recebida
    print(f"\n{body.decode()}")
    print("\nAguarde novas atualizações ou escolha outra opção escrevendo 'Menu'.")


def menu(channel):
    print("Deseja ouvir sobre alguma categoria em específico?")
    print("1) Atualizações Gerais")
    print("2) Saúde")
    print("3) Limpeza")
    print("4) Diversão")
    print("5) Feedback")
    print("6) Alimentação")
    print("0) Voltar para o Menu")

    opcao = int(input())

    if opcao == 1:
        routing_key = "#"
    elif opcao == 2:
        routing_key = "saude"
    elif opcao == 3:
        routing_key = "limpeza"
    elif opcao == 4:
        routing_key = "diversao"
    elif opcao == 5:
        routing_key = "feedback"
    elif opcao == 6:
        routing_key = "alimentacao"
    elif opcao == 0:
        print("\nVoltando ao menu principal...")
        return
    else:
        print("\nOpção inválida! Tente novamente.")
        return menu(channel)

    queue = channel.queue_declare('', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue,
                       routing_key=routing_key)
    print("\nAguardando mensagens do PetJoy Hotel...")

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


# Ações do Consumidor:
print("Bem-vindo(a) ao canal de comunicação do PetJoy!")
print("Você está antenado nas informações gerais do nosso hotelzinho!")
menu(channel)
