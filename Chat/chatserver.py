# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import time

# import cryptography modules
from cryptography.fernet import Fernet
import base64
import hashlib

import os


class server_crypto:
    def __init__(self, key = None): # Initialize
        self.key = key
        self.cryptor = None

    def keygen(self): # key generation
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)
        with open('Key', 'wb+') as f:
            f.write(self.key)
            f.close()

    def readkey(self): # read key
        with open('Key', 'rb') as f:
            self.key = f.read()
            self.cryptor = Fernet(self.key)
            f.close()
    def encrypt(self, msg): # encrypt communication
        msg = self.cryptor.encrypt(msg)
        msg = base64.b64encode(msg)
        return msg# import socket programming library
import socket

# import thread module
from _thread import *
import threading
import time

# import cryptography modules
from cryptography.fernet import Fernet
import base64
import hashlib

import os

# cryptography object for server
class server_crypto:
    def __init__(self, key = None): # Initialize
        self.key = key
        self.cryptor = None

    def keygen(self): # key generation
        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)
        with open('Key', 'wb+') as f:
            f.write(self.key)
            f.close()

    def readkey(self): # read key
        with open('Key', 'rb') as f:
            self.key = f.read()
            self.cryptor = Fernet(self.key)
            f.close()
    def encrypt(self, msg): # encrypt communication
        msg = self.cryptor.encrypt(msg)
        msg = base64.b64encode(msg)
        return msg
    def decrypt(self, msg): # decrypt communication
        msg = base64.b64decode(msg)
        msg = self.cryptor.decrypt(msg)
        return msg
    def send(self, msg, c):
        c.send(self.encrypt(msg.encode('utf-8')))
    def receive(self, c):
        data = c.recv(1024)
        data = self.decrypt(data).decode('utf-8')
        return data

# buffer storing (temp) communication data
class Buffer:
    def __init__(self):
        self.buffer = []
        self.cl = []
        self.cl_list = []
        self.addrbook = []
    def write(self,msg):
        self.buffer.append(msg)
    def remove(self,msg):
        self.buffer.remove(msg)
    def read(self):
        return self.buffer
    def clear(self):
        self.buffer = []

# check and delete offline sockets
def checkmembers(bf):
    clients = bf.cl
    for client in clients:
        if client.fileno() < 0:
            idx = bf.cl.index(client)
            print(f'\n{bf.addrbook[idx][0]} {bf.addrbook[idx][1]} {bf.addrbook[idx][2]} exited\n')

            bf.cl.remove(client)
            bf.addrbook.remove(bf.addrbook[idx])


# send message to other clients + kick clients
def log(c, crypto, bf, rm):
    try:
        print(''.join(bf.buffer))
        clients = bf.cl
        #print(clients)
        if rm == True:
            for client in clients:
                if client != c:
                    try:
                        client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
                    except:
                        pass
        else:
            for client in clients:
                try:
                    client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
                except:
                    pass
        bf.clear()
    except Exception as e:
        bf.clear()
        pass

# program to run after a client send a message
def user_agent(c, crypto, bf, clientnum, addr, name):
    bf.addrbook.append([name, addr[0], addr[1]])
    try:
        while True:
            data = crypto.decrypt(c.recv(1024)).decode('utf-8')
            checkmembers(bf)
            if len(data) == 0:
                c.send(crypto.encrypt("Warning: No data sended".encode('utf-8')))
                continue
            if len(data.strip().split(': ')) > 1:
                if data.strip().split(': ')[1] == '!exit':
                    clientnum -= 1
                    print(f'\nclient {c} exited\n')
                    bf.cl.remove(c)
                    c.close()
                else:
                    bf.write(data)
                    start_new_thread(log, (c, crypto, bf, True))
    except:
        pass
    c.close()

def show_options():
    print('''

    Chat server is online!

    To send a message, just type your message and press enterself.

    To execute a command, type a colon and a space to separate command and parameters.

    !<command>: <parameters>

    Eg: !kick: 12345

    A list of options:

    1) kick a member from the server
        !kick: <IDX>
    2) show connected clients
        !show
    3) send info notifications
        !sendinfo: <message>
    4) send warning notifications
        !sendwarning: <message>


    ''')

# server communication interface
def console(c, crypto, bf, clientnum):
    print("console is running")
    while True:
        data = '\nServer: ' + input() + '\n'
        checkmembers(bf)
        if len(data.strip().split(': ')) > 1:
            if data.strip().split(': ')[1] == '!kick':
                try:
                    print('Kicking')
                    idx = int(data.strip().split(': ')[2])
                    conn = bf.cl_list[idx][1]
                    bf.cl.remove(conn)
                    conn.close()
                    clientnum -= 1
                    print('client successfully kicked\n')
                    bf.addrbook.remove(bf.addrbook[idx])
                except Exception as e:
                    print(f'Error in kicking members: {e}')
            elif data.strip().split(': ')[1] == '!show':
                print('\nIDX   name      IP           port')
                for client in bf.addrbook:
                    print(f' {bf.addrbook.index(client)}   {client[0]}  {client[1]}  {client[2]}')

            elif data.strip().split(': ')[1] == '!sendinfo':
                msg = 'Info: ' + ': '.join(data.strip().split(': ')[2:])
                bf.write(msg)
                start_new_thread(log, (c, crypto, bf, False))

            elif data.strip().split(': ')[1] == '!sendwarning':
                msg = 'Warning: ' + ': '.join(data.strip().split(': ')[2:])
                bf.write(msg)
                start_new_thread(log, (c, crypto, bf, False))

            elif data.strip().split(': ')[1] == '!help':
                show_options()
            else:
                bf.write(data)
                start_new_thread(log, (c, crypto, bf, False))

# authentication program
def auth(c, crypto, bf, clientnum, addr):
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

            if ans.strip().decode('utf-8') == hashlib.sha1(b"Daniel").hexdigest():
                name = crypto.decrypt(c.recv(1024)).strip().decode('utf-8')

                msg = f'Info: client {addr[0]} {addr[1]} authenticated'
                bf.write(msg)
                start_new_thread(log, (c, crypto, bf, True))
                start_new_thread(user_agent, (c, crypto, bf, clientnum, addr, name))
                succ = crypto.encrypt( (banner+'\n').encode('utf-8'))
                c.send(succ)
                break
            else:
                time.sleep(1)
                c.send(crypto.encrypt('Nope!!!\n'.encode('utf-8')))
                clientnum -= 1
                bf.cl_list.remove(bf.cl_list[bf.cl.index(c)])
                bf.cl.remove(c)

                c.close()


    except Exception as e:
        print(f'Authentication failed: {e}')
        clientnum -= 1
        bf.cl_list.remove(bf.cl_list[bf.cl.index(c)])
        bf.cl.remove(c)
        #del bf.addrbook[addr[1]]

        c.close()


def Main():
    consolenum = 0 # number of consoles (should be either 0 or 1)
    clientnum = 0 # of client can connect to the server
    crypto = server_crypto() # server cryptography module
    bf = Buffer() # chat record buffer

    # to find the key file and read it
    if not os.path.isfile('Key'):
        print('Generating key')
        crypto.keygen()
    else:
        print('Keyfile already exists ')
        act = input("Do you wanted to generate a new key?[Y/n] ")
        if act == 'Y':
            crypto.keygen()
        else:
            crypto.readkey()
    host = "" #listen on every interface

    # reverse a port on your computer
    port = 1000
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
            bf.cl_list.append([str(addr[1]), c])

            try:
                if 1:# < 3:
                    start_new_thread(auth, (c, crypto, bf, clientnum, addr)) # start user auth in background
                    clientnum += 1
                else:
                    c.close()
                if consolenum < 1:
                    # start server side interface in background
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

    def decrypt(self, msg): # decrypt communication
        msg = base64.b64decode(msg)
        msg = self.cryptor.decrypt(msg)
        return msg
    def send(self, msg, c):
        c.send(self.encrypt(msg.encode('utf-8')))
    def receive(self, c):
        data = c.recv(1024)
        data = self.decrypt(data).decode('utf-8')
        return data

def checkmembers(bf):
    clients = bf.cl
    for client in clients:
        if client.fileno() < 0:
            bf.cl.remove(client)

# send message to other clients + kick clients
def log(c, crypto, bf, rm):
    try:
        checkmembers(bf)
        print(''.join(bf.buffer))
        clients = bf.cl
        #print(clients)
        if rm == True:
            for client in clients:
                if client != c:
                    try:
                        client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
                    except:
                        pass
        else:
            for client in clients:
                try:
                    client.send(crypto.encrypt(''.join(bf.read()).encode('utf-8')))
                except:
                    pass
        bf.clear()
    except Exception as e:
        bf.clear()
        pass

# program to run after a client send a message
def user_agent(c, crypto, bf, clientnum):
    try:
        while True:
            data = crypto.decrypt(c.recv(1024)).decode('utf-8')
            if len(data.strip().split(': ')) > 1:
                if data.strip().split(': ')[1] == 'exit':
                    clientnum -= 1
                    print(f'client {c} exited')
                    bf.cl.remove(c)
                    c.close()
                else:
                    bf.write(data)
                    start_new_thread(log, (c, crypto, bf, True))
    except:
        pass
    c.close()


# server communication interface
def console(c, crypto, bf, clientnum):
    print("console is running")
    while True:
        data = '\nServer: ' + input() + '\n'
        if len(data.strip().split(': ')) > 1:
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

# authentication program
def auth(c, crypto, bf, clientnum, addr):
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

            if ans.strip().decode('utf-8') == hashlib.sha1(b"Daniel").hexdigest():
                msg = f'Info: client {addr[0]} {addr[1]} authenticated'
                bf.write(msg)
                start_new_thread(log, (c, crypto, bf, True))
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

# buffer storing (temp) communication data
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
    def clear(self):
        self.buffer = []

def Main():
    consolenum = 0 # number of consoles (should be either 0 or 1)
    clientnum = 0 # of client can connect to the server
    crypto = server_crypto() # server cryptography module
    bf = Buffer() # chat record buffer

    # to find the key file and read it
    if not os.path.isfile('Key'):
        print('Generating key')
        crypto.keygen()
    else:
        print('Keyfile already exists ')
        act = input("Do you wanted to generate a new key?[Y/n]")
        if act == 'Y':
            crypto.keygen()
        else:
            crypto.readkey()
    host = "" #listen on every interface

    # reverse a port on your computer
    port = 5555
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
                if 1:# < 3:
                    start_new_thread(auth, (c, crypto, bf, clientnum, addr)) # start user auth in background
                    clientnum += 1
                else:
                    c.close()
                if consolenum < 1:
                    # start server side interface in background
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
