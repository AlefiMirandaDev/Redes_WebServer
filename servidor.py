import socket
import threading

#from http.server import BaseHTTPRequestHandler, HTTPServer

#host = '10.99.119.246'
port = 13500

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('',port))
servidor.listen(0)

print(f'\t\tDados do Servidor\t\n\n\tHost:******\n\tPort:{port}\n')
print('Servidor Online pronto para receber...\n')

#Pegando coneção do cliente
def connect(connect_cliente, addr):
    print(f'Conexão vinda de {addr}')

    #name_page = connect_cliente.recv(2048)
    #NP_Decode = name_page.decode('utf-8')
    #print(f'NAME PAGE: {NP_Decode}')

    #connect_cliente.send(NP_Decode)   
    connect_cliente.close()

def main():

    while True:
        
        connect_cliente, addr = servidor.accept()

        serv_th = threading.Thread(target=connect, args=(connect_cliente, addr))
        serv_th.start()



if __name__ == '__main__':
    main()