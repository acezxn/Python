# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import time
from cryptography.fernet import Fernet
import os
import base64

class server_crypto:
    def __init__(self, key = None):
        self.key = key
        self.cryptor = None

    def keygen(self):
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)
        with open('Key', 'wb+') as f:
            f.write(self.key)
            f.close()

    def readkey(self):
        with open('Key', 'rb') as f:
            self.key = f.read()
            self.cryptor = Fernet(self.key)
            f.close()
    def encrypt(self, msg):
        msg = self.cryptor.encrypt(msg)
        msg = base64.b64encode(msg)
        return msg
    def decrypt(self, msg):
        msg = base64.b64decode(msg)
        msg = self.cryptor.decrypt(msg)
        return msg

# thread fuction
def log(c, crypto, bf, rm):
    try:
        print(''.join(bf.buffer))
        clients = bf.cl
        if rm == True:
            clients.remove(c)
            for client in clients:
                client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
            clients.append(c)
        else:
            for client in clients:
                client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
        bf.buffer.remove(bf.read()[0])
    except:
        pass


def user_agent(c, crypto, bf, clientnum):
    try:
        while True:
            data = crypto.decrypt(c.recv(1024)).decode('utf-8')
            if data.strip().split(': ')[1] == 'exit':
                clientnum -= 1
                bf.cl.remove(c)
                c.close()
            else:
                bf.write(data)
                start_new_thread(log, (c, crypto, bf, True))
    except:
        pass
    c.close()


def console(c, crypto, bf, clientnum):
    print("console is running")
    while True:
        data = '\nServer: ' + input() + '\n'
        if data.strip().split(': ')[1] == 'kick':
            try:
                print('Kicking')
                conn = bf.cl_dict[data.strip().split(': ')[2]]
                bf.cl.remove(conn)
                conn.close()
                clientnum -= 1
            except Exception as e:
                print(f'Error in kicking members: {e}')
        else:
            bf.write(data)
            start_new_thread(log, (c, crypto, bf, False))
            data = crypto.encrypt(data.encode('utf-8'))

def auth(c, crypto, bf, clientnum):
    banner = '''

=======================================
Access Granted! Welcome to anon channel
=======================================
|  You may type message to everyone on the server below
V  You can get access to conversations
    '''
    try:
        print('Started Authentication')
        time.sleep(1)
        title = crypto.encrypt('Insert password\n'.encode('utf-8'))
        c.send(title)
        while True:
            ans = crypto.decrypt(c.recv(1024))
            if ans.strip().decode('utf-8').split(': ')[1] == "Daniel":
                start_new_thread(user_agent, (c, crypto, bf, clientnum))
                succ = crypto.encrypt( (banner+'\n').encode('utf-8'))
                c.send(succ)
                break
            else:
                time.sleep(1)
                c.send(crypto.encrypt('Nope!!!\n'.encode('utf-8')))
                clientnum -= 1
                bf.cl.remove(c)
                c.close()
    except Exception as e:
        print(f'Authentication failed: {e}')
        clientnum -= 1
        bf.cl.remove(c)
        c.close()

class Buffer:
    def __init__(self):
        self.buffer = []
        self.cl = []
        self.cl_dict = {None:None}
    def write(self,msg):
        self.buffer.append(msg)
    def remove(self,msg):
        self.buffer.remove(msg)
    def read(self):
        return self.buffer


def Main():
    consolenum = 0
    clientnum = 0
    crypto = server_crypto()
    bf = Buffer()
    if not os.path.isfile('Key'):
        print('Generating key')
        crypto.keygen()
    else:
        crypto.readkey()
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 5432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)
    # put the socket into listening mode
    s.listen(5)
    print("socket is listening")

    # a forever loop until client wants to exit
    while True:

        # establish connection with client
        try:
            c, addr = s.accept()
            bf.cl.append(c)
            # lock acquired by client
            print('Connected to :', addr[0], ':', addr[1])
            bf.cl_dict.update({str(addr[1]): c})
            try:
                if clientnum < 3:
                    start_new_thread(auth, (c, crypto, bf, clientnum))
                    clientnum += 1
                else:
                    c.close()
                if consolenum < 1:
                    start_new_thread(console, (c, crypto, bf, clientnum))
                    consolenum = 1
                else:
                    pass
            except:
                pass
        except KeyboardInterrupt:
            s.close()


if __name__ == '__main__':
    Main()
