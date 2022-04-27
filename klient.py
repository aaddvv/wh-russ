import socket
from Tkinter import *
tk=Tk()
labell = Label(text="login")
labelll = Label(text="password")
loggin = Entry(foreground="black",background="gold")
passw = Entry(foreground="black",background="gold")

def sklog():
	fff = loggin.get()
	hhh = passw.get()
	labell.pack_forget()
	loggin.pack_forget()
	labelll.pack_forget()
	passw.pack_forget()
	baton.pack_forget()


	import mess
baton = Button(
text="login",
    width=25,
    height=5,
    bg="gold",
    fg="black",
    command=sklog,
)
labell.pack()
loggin.pack()
labelll.pack()
passw.pack()
baton.pack()

tk.mainloop()
#pack_forget
#import mess
