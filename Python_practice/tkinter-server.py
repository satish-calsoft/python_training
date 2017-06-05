from Tkinter import *
import socket
from threading import *
from ScrolledText import*

class Receive():
    def __init__(self,server,textarea):
        self.server = server
        self.textarea = textarea
        while 1:
            text = self.server.recv(1024)
            if not text: break
            self.textarea.insert(END,'client >> %s\n'%text)
class Application(Thread):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    host = "" # Get local machine name
    port = 12343               # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    s.listen(2000)                 # Now wait for client connection.
    c, addr = s.accept()     # Establish connection with client.
    print c,addr
    
    def __init__(self, form):
        Thread.__init__(self)
        form.resizable(0,0)
        form.minsize(200, 200)
        form.title("Server::")
        
        
        # Global Padding pady and padx
        pad_x = 5
        pad_y = 5        
        
        button1 = Button(form, text='Send', command = self.addchat)
        
        label1 = Label(form, text="Label1")
        textbox1 = Entry(form)    
        
        textarea1 = Text(form, width=20, height=10)
        
        
        self.textbox = textbox1 # to make it accessible outside your __init__
        self.textarea = textarea1 # see above
        
        self.textarea.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky=W)
        self.textbox.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky=W)
        button1.grid(row=1, column=2, padx=pad_x, pady=pad_y, sticky=W) 
        
        form.bind("<Return>", lambda x: self.addchat())   
    
    
    def addchat(self):
        
        txt = self.textbox.get()
        # gets everything in your textbox
        self.textarea.insert(END,'Me >> %s \n'%txt)
        # tosses txt into textarea on a new line after the end
        self.c.send(txt)
        self.textbox.delete(0,END) # deletes your textbox text   
    
    def run(self):
        Receive(self.c, self.textarea)    
 

root = Tk()
app = Application(root).start()
root.mainloop()