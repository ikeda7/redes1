import socket

# Configurações do servidor
host = 'localhost'
port = 12345

# Cria um socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((host, port))
print('Servidor UDP esperando por pacotes...')

while True:
    # Recebe pacote e endereço do cliente
    data, addr = udp_socket.recvfrom(1024)
    print('Pacote recebido do cliente:', data.decode())

    # Responde ao cliente
    response = 'Servidor UDP recebeu o pacote: ' + data.decode()
    udp_socket.sendto(response.encode(), addr)

    # Encerra a conexão se o pacote for 'exit'
    if data.decode() == 'exit':
        break

# Fecha o socket
udp_socket.close()
