package com.petjoy;

import com.rabbitmq.client.*;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Produtor {
    private static final String EXCHANGE_NAME = "pet_joy_hotelzinho";

    public static String menuCategoria(Scanner scanner) {
        String tipo = "";

        while (true) {
            System.out.println("\nEscolha a categoria:");
            System.out.println("1 - Alimentação");
            System.out.println("2 - Saúde");
            System.out.println("3 - Limpeza");
            System.out.println("4 - Diversão");
            System.out.println("5 - Feedback");
            System.out.print("Digite o número correspondente à sua opção: ");

            int categoria = scanner.nextInt();
            scanner.nextLine();

            switch (categoria) {
                case 1 -> tipo = "alimentacao";
                case 2 -> tipo = "saude";
                case 3 -> tipo = "limpeza";
                case 4 -> tipo = "diversao";
                case 5 -> tipo = "feedback";
                default -> {
                    System.out.println("Opção inválida! Tente novamente.");
                    continue;
                }
            }
            break;
        }
        return tipo;
    }

    private static String capitalize(String str) {
        if (str == null || str.isEmpty())
            return str;
        return str.substring(0, 1).toUpperCase() + str.substring(1);
    }

    public static void main(String[] argv) throws Exception {
        Scanner scanner = new Scanner(System.in);
        String tipo;

        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("jackal-01.rmq.cloudamqp.com");
        factory.setUsername("pzfafvhx");
        factory.setPassword("o5wRgx64SsXd1RI50ZcXxKeT1QdAFi0P");
        factory.setVirtualHost("pzfafvhx");
        factory.setPort(5671);
        factory.useSslProtocol();

        try (Connection connection = factory.newConnection();
                Channel channel = connection.createChannel()) {

            channel.exchangeDeclare(EXCHANGE_NAME, "topic");

            System.out.println("\nOlá Cuidador(a) PetJoy, bem-vindo(a)!");
            System.out.print("Digite seu nome: ");
            String cuidador = scanner.nextLine();

            while (true) {
                tipo = menuCategoria(scanner);
                System.out.print("Digite a mensagem: ");
                String corpo = scanner.nextLine();

                String data = new SimpleDateFormat("dd/MM/yyyy - HH:mm").format(new Date());
                String mensagem = String.format("[%s] %s - %s: %s",
                        data, cuidador, capitalize(tipo), corpo);

                String routingKey = tipo;

                channel.basicPublish(EXCHANGE_NAME, routingKey, null, mensagem.getBytes("UTF-8"));
                System.out.println("Mensagem enviada com sucesso!\n");
            }
        }
    }
}
