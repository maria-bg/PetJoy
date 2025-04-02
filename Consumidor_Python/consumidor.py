import pika

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
    print("\nAguarde novas atualizações ou escolha outra opção.")


def menu(cachorro, channel):
    print("\nO que você deseja saber?")
    print("1) Ouvir sobre seu pet (atualizações específicas)")
    print("2) Ouvir mensagens gerais (para todos os pets)")
    opcao = int(input())

    # Definindo a routing key dependendo da opção
    if opcao == 1:
        routing_key = f"#.{cachorro}"
        menuFiltrado(cachorro, channel)
        return
    elif opcao == 2:
        routing_key = "#.*"

    elif opcao == 0:
        print("\nVoltando ao menu principal...")
        return
    else:
        print("\nOpção inválida! Tente novamente.")
        return menu(cachorro, channel)

    queue = channel.queue_declare('', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue,
                       routing_key=routing_key)
    print("\nAguardando mensagens'...")

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


def menuFiltrado(cachorro, channel):
    print(f"Você está ouvindo tudo sobre {cachorro.capitalize()}!")
    print("Deseja ouvir sobre alguma categoria em específico?")
    print("1) Atualizações Gerais")
    print("2) Saúde")
    print("3) Limpeza")
    print("4) Diversão")
    print("5) Feedback")
    print("6) Alimentação")
    print("0) Voltar para o Menu")

    opcaoFiltrada = int(input())

    if opcaoFiltrada == 1:
        routing_key = f"#.{cachorro}"  # Mensagens gerais para todos os donos
    elif opcaoFiltrada == 2:
        routing_key = f"saude.{cachorro}"
    elif opcaoFiltrada == 3:
        routing_key = f"limpeza.{cachorro}"
    elif opcaoFiltrada == 4:
        routing_key = f"diversao.{cachorro}"
    elif opcaoFiltrada == 5:
        routing_key = f"feedback.{cachorro}"
    elif opcaoFiltrada == 6:
        routing_key = f"alimentacao.{cachorro}"
    elif opcaoFiltrada == 0:
        print("\nVoltando ao menu principal...")
        return
    else:
        print("\nOpção inválida! Tente novamente.")
        return menu(cachorro, channel)

    queue = channel.queue_declare('', exclusive=True).method.queue
    channel.queue_bind(exchange=exchange_name, queue=queue,
                       routing_key=routing_key)
    print(f"\nAguardando mensagens sobre '{cachorro.capitalize()}'...")

    channel.basic_consume(
        queue=queue, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()


# Ações do Consumidor:
print("Bem-vindo(a) ao canal de comunicação do PetJoy!")
print("Para saber as atualizações do seu pet hospedado, digite o nome dele(a) abaixo:")
cachorro = input().strip().lower()
menu(cachorro, channel)
