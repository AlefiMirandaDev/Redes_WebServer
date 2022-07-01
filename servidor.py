import socket,threading
from http.server import BaseHTTPRequestHandler, HTTPServer

host = '10.99.119.246'
port = 13500

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('',port))
servidor.listen(0)

#webbrowser.open_new_tab('~/Documentos/servidor_web/pages/page_3.html')

print(f'\t\tDados do Servidor\t\n\n\tHost:{host}\n\tPort:{port}\n')
print('Servidor Online pronto para receber...\n')

def connect(connect_cliente, addr):
    #Pegando coneção do cliente
    print(f'Conexão vinda de {addr}')

    name_page = connect_cliente.recvfrom(2048)
    NP_Decode = name_page.decode('utf-8')
        
    print(f'NAME PAGE: {NP_Decode}')
        
    connect_cliente.close()

def main():

    while True:
        
        connect_cliente, addr = servidor.accept()

        th = threading.Thread(target=connect, args=(connect_cliente, addr))
        th.start()


if __name__ == '__main__':
    main()
    
#    servidor.close()
    


    # def handle_request(request):
    #     headers = request.split('\n')
    #     filename = headers[0].split()[1]
    #     if filename == '/':
    #         filename = '/index.html'

    #     try:
    #             fin = open('htdocs' + filename)
    #             content = fin.read()
    #             fin.close()

    #             response = 'HTTP/1.0 200 OK\n\n' + content
    #     except FileNotFoundError:
    #             response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found 2'

    #     return response
