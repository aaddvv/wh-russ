# -*- coding: utf-8 -*- 
#from klient import *
from Tkinter import *
import socket
reload(sys)
sys.setdefaultencoding('utf-8')
#-----------------------------
tkk = Tk()

def getip():
        iip = socket.gethostbyname(socket.gethostname())
        return iip
#fff = loggin.get()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('192.168.19.255',11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

#sock.sendto (getip(),('192.168.19.255',11718))

text=StringVar()
name=StringVar()
name.set('user')
text.set('')
tkk.title('WH-RUSS')
tkk.geometry('500x400')

log = Text(tkk,foreground="black",background="cyan")
nick = Entry(tkk, textvariable=name,foreground="black",background="gold")
msg = Entry(tkk, textvariable=text,foreground="black",background="gold")
msg.pack(side='bottom', fill='x', expand='true')
nick.pack(side='bottom', fill='x', expand='true')
log.pack(side='top', fill='both',expand='true')

def loopproc():
	log.see(END)
	s.setblocking(False)
	try:
		message = s.recv(128)
		log.insert(END,message+'\n')
	except:
		tkk.after(1,loopproc)
		return
	tkk.after(1,loopproc)
	return

def iipp():
	myhostt = str(getip())
	resultt = "|" + myhostt
	return resultt 
def sendproc(event):
	text.set(msg.get())
	sock.sendto ("@"+name.get()+':'+text.get()+iipp(),('192.168.19.255',11719))
#	sock.sendto (name.get()+':'+text.get(),('127.0.0.1',11719))
	name.set(nick.get())
	text.set('')
#	ipp = getip()
#	sock.sendto (ipp,('192.168.19.255',11719))

msg.bind('<Return>',sendproc)

msg.focus_set()

tkk.after(1,loopproc)
tkk.mainloop()
