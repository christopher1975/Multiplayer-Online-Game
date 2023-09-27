import socket
import pickle   #agar data antar client tetap sama

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.56.1"  #set IP
        self.port = 5555    #set port
        self.addr = (self.host, self.port)  #set address
        self.p = self.connect()     #connect to server

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)      #connect to server
            return pickle.loads(self.client.recv(2048))
        except:
            pass     

    def send(self, data):
        self.client.send(pickle.dumps(data))    #send data
        return pickle.loads(self.client.recv(2048))
