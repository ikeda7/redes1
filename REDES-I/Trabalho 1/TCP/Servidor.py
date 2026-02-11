import socket

# Configurações do servidor
host = socket.gethostname()
port = 12345

# Cria um socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((host, port))
tcp_socket.listen(1)
print('Servidor TCP esperando por conexões...')

# Aceita a conexão do cliente TCP
conn, addr = tcp_socket.accept()
print('Conexão TCP estabelecida com o cliente:', addr)

while True:
    # Recebe mensagem do cliente
    data = conn.recv(1024).decode()
    print('Mensagem recebida do cliente:', data)

    # Responde ao cliente
    response = 'Servidor TCP recebeu a mensagem: ' + data
    conn.send(response.encode())

    # Encerra a conexão se a mensagem for 'exit'
    if data == 'exit':
        break

# Fecha o socket
tcp_socket.close()
