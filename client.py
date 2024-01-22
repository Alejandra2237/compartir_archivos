#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096
#GUI
name = None
list_box = None
text_area = None
label_chat = None
text_message = None

def open_Chat_Window():
    #create window
    window = Tk()
    window.title("Messenger")
    window.geometry("500x300")

    #label name
    name_label = Label(window, text="Ingresa tu nombre", font = ("Calibri",10))
    name_label.place(x=10, y=8)

    #Entry text name
    name = Entry(window, width=30, font=("Calibri", 10))
    name.place(x=120,y=8)
    name.focus()

    #Button connect to server
    connect_server = Button(window, text="Conectar al servidor de chat", bd =1, font = ("Calibri",10))
    connect_server.place(x=350,y=6)

    #Separator
    separator = ttk.Separator(window, orient="horizontal")
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    #Button conection
    connect_button = Button(window, text="Conectar", bd =1, font = ("Calibri",10 ))
    connect_button.place(x=282,y=160)

    #Button disconection
    disconnect_button = Button(window, text="Desconectar", bd =1, font = ("Calibri",10 ))
    disconnect_button.place(x=350,y=160)

    #Button refresh
    refresh = Button(window, text="Actualizar", bd =1, font = ("Calibri",10 ))
    refresh.place(x=435,y=160)

    #mainloop 
    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    open_Chat_Window()


setup()


#-----------Bolierplate Code Start -----