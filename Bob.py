import socket

HOST = socket.gethostname()
PORT = 12345

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST
        self.port = PORT
        self.sock.connect((self.host, self.port))
        print("Connected to Server ... ")
        self.connection_handler()

    def  connection_handler(self):
        while True:


    def display(self):
        print("message set : ")
        print(self.messages)
