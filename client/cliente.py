import socket
import webbrowser

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.1.104'
port = 5800

client.connect((host, port))
print(f'Conectado ao servidor {host}\n')

namefile = str(input('arquivo: '))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)
print(f'{namefile} recebido\n')

webbrowser.open_new_tab(namefile)
