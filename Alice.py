import numpy as np
from ECC import *

import socket

PORT = 12345

class Alice:

    def __init__(self):
        self.name = "Alice"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = socket.gethostname()
        self.port = PORT
        self.sock.bind((self.host, self.port))
        self.aecc = ECC(2, 3, 67)


    def connection_handler(self, conn):
        while True:
            data = conn.recv(1024).decode
            if data == "send_public_key":
                conn.send(str(self.aecc.public_key).encode())
            else:
                self.aecc.decryption(data)


    def listener(self):
        print("Alice is running waiting for connection with the public key")
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        self.connection_handler(conn)