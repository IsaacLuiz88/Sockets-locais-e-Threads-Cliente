import socket
import uuid

HOST = '127.0.0.1'
PORT = 65432

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    # Envia um identificador único ao servidor
    client_id = str(uuid.uuid4())
    print(f"Seu identificador: {client_id}")
    client.sendall(client_id.encode('utf-8'))

    try:
        print("Digite mensagens para enviar ao servidor. Pressione Ctrl+C para sair.")
        while True:
            # Lê mensagem do usuário
            message = input("> ")
            if not message:
                print("Mensagem vazia. Encerrando...")
                break
            
            client.sendall(message.encode('utf-8'))

    except KeyboardInterrupt:
        print("\nEncerrando cliente...")

    finally:
        client.close()
        print("Cliente desconectado.")

if __name__ == "__main__":
    start_client()
