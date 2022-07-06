import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5800

server.bind(("", port))
print("servidor ONLINE")

server.listen(0)

connection, address = server.accept()

namefile = connection.recv(1024).decode('utf-8')

with open(namefile, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('arquivo enviado')