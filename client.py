from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import *




def receive():
    """Handles receiving of messages."""
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  # Possibly client has left the chat.
            break


def send(event=None):  # event is passed by binders.
    """Handles sending of messages."""
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    """This function is to be called when the window is closed."""
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.geometry("400x600")

big = LabelFrame(top,text='',padx=15,pady=15,bg='black')
big.pack(padx=10,pady=10)




frames2= LabelFrame(big,text='',padx=10,pady=10,bg="gold")
frames2.pack(padx=10,pady=10)

frames1 = LabelFrame(big,text='',padx=10,pady=10,bg="gold")
frames1.pack(padx=10,pady=10)


frames = LabelFrame(big,text='',padx=1,pady=1,bg="gold")
frames.pack(padx=10,pady=10)




#messages_frame = tkinter.Frame(top,bg='green')
my_msg = tkinter.StringVar()  # For the messages to be sent.
scrollbar = tkinter.Scrollbar(frames2)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(frames2, height=15, width=50,yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
frames2.pack()
entry_field = tkinter.Entry(frames1, textvariable=my_msg,width=40,borderwidth=5)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(frames1, text="Send", command=send,padx=45,pady=5)
send_button.pack(padx=10,pady=10)


top.protocol("WM_DELETE_WINDOW", on_closing)

#----Now comes the sockets part----
HOST = '127.0.0.1'
PORT = '33000'
if not PORT:
    PORT = 33000
else:
    PORT = int(PORT)

BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()  # Starts GUI execution.
