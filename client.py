#Cliente envia o nome da pagina que ele quer e o servidor devolve o arquivo com um diretorio

import socket, threading, time, random
import webbrowser

host = '10.99.119.246'
port = 13500

print('\t\tCliente Teste')

def connect(i):
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((host,port))

    name_page = input('Name Page: ')

    time.sleep(random.randint(11,20))

    cliente.send(name_page.encode('utf-8'))
    
    Mod_NP = cliente.recv(2048).decode('utf-8')
    print(f'{Mod_NP}')

    time.sleep(random.randint(1,10))

    cliente.close()

def main():
    for i in range(1,11):
        client_th = threading.Thread(target=connect, args=[i])
        client_th.start()
        time.sleep(random.randint(1,10))

if __name__ == '__main__':
    main()