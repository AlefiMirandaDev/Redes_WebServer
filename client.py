#Cliente envia o nome da pagina que ele quer e o servidor devolve o arquivo com um diretorio

import socket
import webbrowser

host = '10.99.119.246'
port = 13500

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host,port))

print('\t\tCliente Teste')

name_page = ''

while(name_page != 'exit'):
       
    name_page = input('Name Page: ')
    cliente.sendto(name_page.encode('utf-8'),(host,port))
    
    
    cliente.close()

    # url_resp =  
    # webbrowser.open_new_tab(url_resp)