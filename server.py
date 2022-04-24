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
def faadd(jj):
        with open('ip.txt', 'a') as file:
                file.write(jj + "\n")
def fscan(ipp):
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
def fadd(fiip):
        rr = fscan(fiip)
        if rr == 1 :
                return
        if rr == 0 :
                faadd(fiip)

def vscan(jh):
	parts = jh.split('|')
	part1 = parts[0]
	part2 = parts[1]  
	fadd (part2)
	scan(part1)
def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	s.bind(('0.0.0.0',11719))
	while 1:
		message = s.recv(128)
		vscan (message)
if __name__ == "__main__":
	main()
