import socket

def str_to_bin(mensagem: str) -> bytes:
    """
    Converte uma string em uma sequência de bits.
    """
    return bytes(''.join(format(ord(char), '08b') for char in mensagem), 'utf-8')

def bin_to_str(sequence: bytes) -> str:
    """
    Converte uma sequência de bits em uma string.
    """
    return ''.join(chr(int(sequence[i:i+8], 2)) for i in range(0, len(sequence), 8))

def gen_checksum(sequence: bytes, k: int, n: int) -> bytes:
    """
    Gera um checksum para uma sequência de bytes dada.
    """
    segments = [int(sequence[i:i+n], 2) for i in range(0, k * n, n)]
    checksum = bin(sum(segments))[2:].zfill(k)
    return sequence + bytes(checksum, 'utf-8')

def check_checksum(sequence: bytes, k: int, n: int) -> (bool, bytes):
    """
    Verifica a validade de um checksum para uma sequência de bytes dada.
    """
    segments = [int(sequence[i:i+n], 2) for i in range(0, k * n, n)]
    checksum = bin(sum(segments))[2:].zfill(k)
    if checksum == sequence[-k:]:
        return True, sequence[:-k]
    else:
        return False, bytes('sequência inválida', 'utf-8')

def gen_crc(sequence: bytes, G: bytes) -> bytes:
    """
    Gera um CRC para uma sequência de bytes e um polinômio gerador dados.
    """
    msg = sequence
    sequence += b'0' * (len(G) - 1)
    sequence = [int(bit) for bit in sequence]
    G = [int(bit) for bit in G]
    for i in range(len(sequence) - len(G) + 1):
        if sequence[i] == 1:
            for j in range(len(G)):
                sequence[i+j] ^= G[j]
    return msg + bytes(''.join(str(bit) for bit in sequence)[-len(G) + 1:], 'utf-8')

def check_crc(sequence: bytes, G: bytes) -> (bool, bytes):
    """
    Verifica a validade de um CRC para uma sequência de bytes e um polinômio gerador dados.
    """
    msg = sequence
    sequence += b'0' * (len(G) - 1)
    sequence = [int(bit) for bit in sequence]
    G = [int(bit) for bit in G]
    for i in range(len(sequence) - len(G) + 1):
        if sequence[i] == 1:
            for j in range(len(G)):
                sequence[i+j] ^= G[j]
    if '1' in ''.join(str(bit) for bit in sequence)[-len(G) + 1:]:
        return False, bytes('sequência inválida', 'utf-8')
    else:
        return True, msg[:len(msg) - len(G) + 1]

def enviar(mensagem: str):
    """
    Envia uma mensagem para um servidor usando o protocolo TCP.
    """
    host = socket.gethostname()
    port = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        mensagem = bytes(mensagem, 'UTF-8')
        s.connect((host, port))
        s.send(mensagem)
        s.close()

def receber():
    """
    Recebe uma mensagem de um cliente usando o protocolo TCP.
    """
    host = socket.gethostname()
    port = 5000
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, addr = s.accept()
        data = conn.recv(1024)
        data = data.decode('utf-8')
        conn.close()
        s.close()
        return data