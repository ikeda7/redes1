import socket

# Configurações do cliente TCP
tcp_host = socket.gethostname()
tcp_port = 12345

# Configurações do cliente UDP
udp_host = socket.gethostname()
udp_port = 54321

# Criação do socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((tcp_host, tcp_port))

# Criação do socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicita mensagem do usuário
    message = input('Digite uma mensagem (ou "exit" para sair): ')

    # Envia mensagem TCP para o servidor
    tcp_socket.send(message.encode())

    if message == 'exit':
        break

    # Recebe resposta TCP do servidor
    tcp_response = tcp_socket.recv(1024)
    print('Resposta do servidor TCP:', tcp_response.decode())

    # Envia mensagem UDP para o servidor
    udp_socket.sendto(message.encode(), (udp_host, udp_port))

    # Recebe resposta UDP do servidor
    udp_response, udp_addr = udp_socket.recvfrom(1024)
    print('Resposta do servidor UDP:', udp_response.decode())

    # Encerra a conexão se a mensagem for 'exit'
    if message == 'exit':
        break

# Fecha os sockets
tcp_socket.close()
udp_socket.close()
