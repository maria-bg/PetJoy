import subprocess


def start_produtor():
    print("\nInicializando Produtor.java\n")
    subprocess.run(
        ["java", "-cp", "Produtor_Java/target/Prodmessenger-0.0.1-SNAPSHOT-jar-with-dependencies.jar", "com.petjoy.Produtor"])


def start_consumidor():
    print("\nInicializando Consumidor.py\n")
    subprocess.run(["python", "Consumidor_Python/consumidor.py"])


def start_auditoria():
    print("\nInicializando Auditoria.py\n")
    subprocess.run(["python", "Auditoria_Python/auditoria.py"])


def menu():
    while True:
        print("\n=== Sistema PetJoy ===")
        print("1. Iniciar Produtor (Cuidador)")
        print("2. Iniciar Consumidor (Dono)")
        print("3. Iniciar Backend de Auditoria")
        print("4. Sair")

        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            start_produtor()
        elif escolha == "2":
            start_consumidor()
        elif escolha == "3":
            start_auditoria()
        elif escolha == "4":
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
