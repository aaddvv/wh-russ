# -*- coding: utf-8 -*- 
import socket
from Tkinter import *
#from tkinter import *
#Решаем вопрос с кирилицей
reload(sys)
sys.setdefaultencoding('utf-8')
#-----------------------------

tk=Tk()
def getip():
        iip = socket.gethostbyname(socket.gethostname())
        return iip

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind(('192.168.19.255',11719))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)

#sock.sendto (getip(),('192.168.19.255',11718))

text=StringVar()
name=StringVar()
name.set('введите здесь свое имя')
text.set('введите здесь свое сообщение')
tk.title('WH-RUSS')
tk.geometry('500x400')

log = Text(tk)
nick = Entry(tk, textvariable=name)
msg = Entry(tk, textvariable=text)
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
		tk.after(1,loopproc)
		return
	tk.after(1,loopproc)
	return

def iipp():
	myhostt = str(getip())
	resultt = "|" + myhostt
	return resultt 
def sendproc(event):
	sock.sendto (name.get()+':'+text.get()+iipp(),('192.168.19.255',11719))
#	sock.sendto (name.get()+':'+text.get(),('127.0.0.1',11719))

	text.set('')
#	ipp = getip()
#	sock.sendto (ipp,('192.168.19.255',11719))

msg.bind('<Return>',sendproc)

msg.focus_set()

tk.after(1,loopproc)
tk.mainloop()
