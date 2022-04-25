import socket
import re
def mess(mes,ippp):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.sendto(mes,(ippp,11719))
#	print(mes)
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
#	print(jj)
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
def findLen(str):
    counter = 0    
    for i in str:
        counter += 1
    return counter
def vscan(jh):
	try:
#		parts = ["admin:admin","127.0.0.1"]
		parts = re.split('|',jh)
		partj = parts[0]
		parts = jh.split('|')
                partj = parts[0]
                partg = parts[1] 
                print("log:/ " + partj)
                print("log:/ " + partg) 
                fadd (partg)
                scan(partj)
	except:
		main()
		print("log:/ error 777-bug to massive not fixed,but all working")
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
