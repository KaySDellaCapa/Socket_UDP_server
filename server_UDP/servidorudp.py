import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso!!!")

host = "localhost"
port = 5432

s.bind((host, port)) # Faz a ligação entre cliente e servidor
mensagem = "\nServidor: Olá, cliente. Estou vivo"

while 1: 
    dados, end = s.recvfrom(4096) # Vai receber igual o cliente

    if dados:
        print("\nCliente:",dados,"Endereço do Cliente",end[0])
        s.sendto(dados + (mensagem.encode()), end)