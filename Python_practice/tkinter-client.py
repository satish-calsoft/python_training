from Tkinter import *
import socket
from threading import *
from ScrolledText import*
import tkMessageBox


class Loginform():
    def __init__(self,form1):
        self.form1 = form1
        self.form1.resizable(0,0)
        self.form1.minsize(200,200)
        self.form1.title("Login")  
        self.loginform()
        self.form1.mainloop()
        
    def loginform(self):
        
        Label(self.form1, text="User Name").grid(row=0)
        Label(self.form1, text="Password").grid(row=1)
        
        username = Entry(self.form1)
        password = Entry(self.form1)
        
        self.username = username
        self.password = password
        
        
        bt1 = Button(self.form1,text ="login",command = lambda:self.validation())
        
        self.username.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.password.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        bt1.grid(row=2, column=1, padx=5, pady=5, sticky=W)
    
    def application(self):
          
        print "in application" 
        
        self.form1.destroy()
        root = Tk()
        app = Application(root).start()
        print app
             
        root.mainloop()
            
    def validation(self):
        print self.username.get()
        
        
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.application()
        else:
            tkMessageBox.showinfo("login","Wrong credentials")
            
  
class Receive():
    
    def __init__(self,server,textarea):
        self.server = server
        self.textarea = textarea
        
        while 1:
            
            text = self.server.recv(1024)
            
            if not text: break
            self.textarea.insert(END,'%s\n'%text)
            self.textarea.see(END)
                    
class Application(Thread):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    host = socket.gethostname() # Get local machine name

    port = 50000              # Reserve a port for your service.``

    s.connect((host, port))
    
    def __init__(self, form):
        Thread.__init__(self)
        form.resizable(0,0)
        form.minsize(200,200)
        form.title(self.host)
        
        # Global Padding pady and padx
        self.pad_x = 5
        self.pad_y = 5        
        Application.form1(self,form)
    
    
    def form1(self,form):
        
        self.form = form
               
    
        
        button1 = Button(self.form, text='Send', command = self.addchat)
        button2 = Button(self.form, text='Quit', command = self.quit)
        
        label1 = Label(self.form, text="Label1")
        textbox1 = Entry(self.form,width=50)    
        
        scrollbar1 = Scrollbar(form)
        
        textarea1 = Text(self.form, width=50, height=20)
        textarea2 = Text(self.form, width=30, height=20)
        
        textarea1.config(yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=textarea1.yview)        
        
        
        self.textbox = textbox1 # to make it accessible outside your __init__
        self.textarea = textarea1 # see above
        self.textarea2 = textarea2
        
        self.textarea.grid(row=0, column=1, padx=self.pad_x, pady=self.pad_y, sticky=W)
        
        scrollbar1.grid(row=0, column=2, padx=self.pad_x, pady=self.pad_y, sticky=W)
        self.textarea2.grid(row=0, column=3, padx=self.pad_x, pady=self.pad_y, sticky=W)
        self.textbox.grid(row=1, column=1, padx=self.pad_x, pady=self.pad_y, sticky=W)
        button1.grid(row=1, column=2, padx=self.pad_x, pady=self.pad_y, sticky=W) 
        button2.grid(row=1, column=3, padx=self.pad_x, pady=self.pad_y, sticky=W) 
        
        self.form.bind("<Return>", lambda x: self.addchat()) 
    
    def addchat(self):
        
        txt = self.textbox.get()
        # gets everything in your textbox
        self.textarea.insert(END,'Me >> %s \n'%txt)
        self.textarea.see(END)
        # tosses txt into textarea on a new line after the end
        self.s.send(txt)
        self.textbox.delete(0,END) # deletes your textbox text   
    
    def run(self):
        
        Receive(self.s, self.textarea)    
    
  
    
    def quit(self):
        
        
        self.form.destroy() 
        Application.s.close()
        import os
        os._exit(1)
        
        
        
        
        
        
        
login = Tk()

Loginform(login)


