import socket
import sys
BUFSIZE = 100

server_address = ('127.0.0.1', 1235)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)
sys.stdout.write(client_socket.recv(BUFSIZE))
#print 'sakderenge'
idNumb = client_socket.recv(BUFSIZE)
print idNumb
sys.stdout.write('>> ')

try:
	while True:
		sys.stdout.write(client_socket.recv(BUFSIZE))
		sys.stdout.write('>> ')
		message = sys.stdin.readline()    
		client_socket.send(message)

except KeyboardInterrupt:
	client_socket.close()
sys.exit(0)
