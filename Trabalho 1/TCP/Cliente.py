import socket

# Configurações do cliente
host = socket.gethostname()
port = 12345

# Cria um socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((host, port))

while True:
    # Solicita mensagem do usuário
    message = input('Digite uma mensagem (ou "exit" para sair): ')

    # Envia mensagem para o servidor
    tcp_socket.send(message.encode())

    if message == 'exit':
        break

    # Recebe resposta do servidor
    response = tcp_socket.recv(1024)
    print('Resposta do servidor:', response.decode())

# Fecha o socket
tcp_socket.close()
