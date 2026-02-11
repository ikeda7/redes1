import socket

# Configurações do cliente
host = 'localhost'
port = 12345

# Cria um socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicita pacote do usuário
    package = input('Digite um pacote (ou "exit" para sair): ')

    # Envia pacote para o servidor
    udp_socket.sendto(package.encode(), (host, port))

    if package == 'exit':
        break

    # Recebe resposta do servidor
    response, _ = udp_socket.recvfrom(1024)
    print('Resposta do servidor:', response.decode())

# Fecha o socket
udp_socket.close()
