import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM protocolo de datagrama

print("Cliente Socket criado com sucesso!!!")

host = "localhost"
port = 5433 # Porta que se conecta com o nosso servidor
mensagem = "Olá, servidor!"

try: 
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) #Encode empacota a mensagem e envia para o servidor

    dados, servidor = s.recvfrom(4096) # O servidor espera uma resposta de 4096bytes
    dados = dados.decode()
    print("Cliente: " + dados)

finally:
    print("Cliente: Fechando conexão")
    s.close()