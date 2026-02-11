import socket

# Configurações do servidor TCP
tcp_host = socket.gethostname()
tcp_port = 12345

# Configurações do servidor UDP
udp_host = socket.gethostname()
udp_port = 54321

# Criação do socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((tcp_host, tcp_port))
tcp_socket.listen(1)

print('Servidor TCP esperando por conexões...')

# Aceita a conexão do cliente TCP
conn, addr = tcp_socket.accept()
print('Conexão TCP estabelecida com o cliente:', addr)

# Criação do socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((udp_host, udp_port))

while True:
    # Recebe mensagem do cliente TCP
    tcp_data = conn.recv(1024).decode()
    print('Mensagem TCP recebida do cliente:', tcp_data)

    # Responde ao cliente TCP
    tcp_response = 'Servidor TCP recebeu a mensagem: ' + tcp_data
    conn.send(tcp_response.encode())

    # Encerra a conexão se a mensagem for 'exit'
    if tcp_data == 'exit':
        break

    # Recebe mensagem do cliente UDP
    udp_data, udp_addr = udp_socket.recvfrom(1024)
    print('Mensagem UDP recebida do cliente:', udp_data.decode())

    # Responde ao cliente UDP
    udp_response = 'Servidor UDP recebeu a mensagem: ' + udp_data.decode()
    udp_socket.sendto(udp_response.encode(), udp_addr)

    # Encerra a conexão se a mensagem for 'exit'
    if udp_data.decode() == 'exit':
        break

# Fecha os sockets
tcp_socket.close()
udp_socket.close()
