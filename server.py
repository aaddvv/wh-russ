import socket

def mess(mes,ippp):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(mes,(ippp,11719))
def scan(mma):
	file1 = open("ip.txt", "r")

	while True:
   		line = file1.readline()

   		if not line:
       	 		break

		resul = line.strip()
		mess(mma,resul)

	file1.close

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',11719))
while 1:
	message = s.recv(128)
	scan (message)
