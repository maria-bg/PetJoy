# PetJoy Hotelzinho 🐶🐱  
Um sistema de comunicação em tempo real entre cuidadores, responsáveis técnicos e um backend de auditoria, usando tópicos no RabbitMQ.

## 📚 Descrição do Projeto  
O sistema simula a comunicação interna de um hotel para pets. Os cuidadores podem enviar mensagens relacionadas a diversas categorias (alimentação, saúde, limpeza, diversão, feedback), que são então roteadas de forma inteligente para os consumidores interessados — sejam responsáveis pelos pets ou sistemas de monitoramento.

Todos os eventos são também registrados por um backend de auditoria.

## 🚀 Tecnologias Utilizadas  
- RabbitMQ (via CloudAMQP)  
- Java (Produtor)  
- Python (Consumidores, Auditoria e Menu)  
- Topic Exchange  
- CLI interativa  

## 🧩 Estrutura do Projeto  
- Produtor (Java): envia mensagens por categoria (routing key).  
- Consumidores (Python): recebem mensagens de uma ou mais categorias.  
- Auditoria (Python): recebe todas as mensagens, independente da categoria.  
- Menu Principal (Python): interface inicial para o usuário escolher o módulo desejado.

## 📌 Categorias e Routing Keys

| Categoria    | Routing Key     |
|--------------|------------------|
| Alimentação  | alimentacao      |
| Saúde        | saude            |
| Limpeza      | limpeza          |
| Diversão     | diversao         |
| Feedback     | feedback         |

O consumidor pode escolher escutar por categoria específica ou por todas (routing key “#”).

## 🛠 Como Executar o Projeto

### 1. Pré-requisitos  
- Java instalado (JDK 11 ou superior)  
- Python 3 instalado  
- Biblioteca Pika (instale via pip):  
  ```bash
  pip install pika
  ```

### 2. Compilando o Produtor (Java)  
Navegue até o diretório do produtor e compile usando Maven:

```bash
cd Produtor_Java
mvn clean compile assembly:single
```

### 3. Executando o Sistema via Menu Principal  
Use o script menu.py para iniciar o projeto e escolher qual parte deseja executar:

```bash
python Menu_PetJoy.py
```

Você verá as seguintes opções:

```
=== Sistema PetJoy ===
1. Iniciar Produtor (Cuidador)
2. Iniciar Consumidor (Dono)
3. Iniciar Backend de Auditoria
4. Sair
```

Escolha a opção desejada para iniciar o respectivo módulo.

## 🧠 Equipe  
- Ian Nunes – ibn@cesar.school  
- Leticia Lopes – 
- Maria Augusta - 
