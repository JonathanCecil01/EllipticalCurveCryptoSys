from EllipticCurve import *
import numpy as np


class ECC:

    def __init__(self, p):
        self.e1 = 0
        self.e2 = 0
        self.d = 4#np.random.randint(p)
        self.p = p
        self.curve = EllipticCurve(2, 3, p)
        self.public_key =[]
        self.key_generation()

    def key_generation(self):
        self.e1 = (2, 22)#self.curve.points[np.random.randint(len(self.curve.points))]
        self.e2 = self.curve.multiply(self.e1, self.d)
        self.public_key =[self.e1, self.e2, self.p]

    def encrypt(self, message):
        r = 6#np.random.randint(self.p)
        c1 = self.curve.multiply(self.e1, r)
        c2 = self.curve.addition(message,self.curve.multiply(self.e2, r))
        return [c1, c2]

    def decrypt(self, message):
        p = self.curve.multiply(message[0], self.d)
        #print(p)
        p = self.curve.inverse(p)
        #print(p)
        p = self.curve.addition(p, message[1])
        return p

    def encryption(self, plainText):
        mapping = []
        cypher = []
        for i in plainText:
            mapping.append(ord(i)-64)
        #print(mapping)
        for i in mapping:
            cypher.append(self.encrypt(self.curve.points[i]))
        return cypher

    def decryption(self, message):
        mapping = []
        plain_text = []
        for i in message:
            mapping.append(self.decrypt(i))
        for i in mapping:
            plain_text.append(chr(self.curve.points.index(i)+64))
        #print(mapping)
        return plain_text



e1 = ECC(67)
#print(e1.public_key)
message = (24, 26)
cypher = e1.encryption("jonathan")
print(cypher)
print(e1.decryption(cypher))
# x = e1.encrypt(message)
# print(x)
# print(e1.decrypt(x))