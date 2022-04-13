import socket 

def aadd(jj):
	with open('ip.txt', 'a') as file:
		file.write(jj + "\n")
def scan(ipp):
        file1 = open("ip.txt", "r")
	result = 0
        while True:
                line = file1.readline()
                if not line:
                        break

                resul = line.strip()
                if resul == ipp :
			result = 1


        file1.close
	return result
def add(iip):
	rr = scan(iip)
	if rr == 1 :
		return
	if rr == 0 :
		aadd(iip)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('0.0.0.0',11718))
while 1:
        ip = s.recv(128)
        add (ip)

