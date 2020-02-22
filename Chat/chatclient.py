import socket

# import thread module
from _thread import *
import threading
import time
from cryptography.fernet import Fernet
import os
import base64
import hashlib

class client_crypto:
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
        msg =  base64.b64encode(msg)
        return msg
    def decrypt(self, msg):
        msg = base64.b64decode(msg)
        msg = self.cryptor.decrypt(msg)
        return msg

def Print_response(s, crypto):
    colors = {'HEADER' : "\033[95m",
    'OKBLUE' : "\033[94m",
    'RED' : "\033[91m",
    'OKYELLOW' : "\033[93m",
    'GREEN' : "\033[92m",
    'LIGHTBLUE' : "\033[96m",
    'WARNING' : "\033[93m",
    'FAIL' : "\033[91m",
    'ENDC' : "\033[0m",
    'BOLD' : "\033[1m",
    'UNDERLINE' : "\033[4m" }
    print('Response printer started')
    while True:
        try:
            data = s.recv(1024)
            data = crypto.decrypt(data).decode('utf-8')
            if data.strip() != 'Insert password' and 'Access Granted' not in data:
                print(colors['WARNING']+ data.split(': ')[0]+ ': '+colors['GREEN']+data.split(': ')[1])
            elif 'Access Granted' in data:
                print('''

      ooooooooooooooooooooooooooooooooooooo
      8                                .d88
      8  oooooooooooooooooooooooooooood8888
      8  8888888888888888888888888P"   8888    oooooooooooooooo
      8  8888888888888888888888P"      8888    8              8
      8  8888888888888888888P"         8888    8             d8
      8  8888888888888888P"            8888    8            d88
      8  8888888888888P"               8888    8           d888
      8  8888888888P"                  8888    8          d8888
      8  8888888P"                     8888    8         d88888
      8  8888P"                        8888    8        d888888
      8  8888oooooooooooooooooooooocgmm8888    8       d8888888
      8 .od88888888888888888888888888888888    8      d88888888
      8888888888888888888888888888888888888    8     d888888888
                                               8    d8888888888
         ooooooooooooooooooooooooooooooo       8   d88888888888
        d                       ...oood8b      8  d888888888888
       d              ...oood888888888888b     8 d8888888888888
      d     ...oood88888888888888888888888b    8d88888888888888
     dood8888888888888888888888888888888888b
                ''')
                print(colors['GREEN']+data)
            else:
                print(colors['GREEN']+data)
        except Exception as e:
            print(f'Print failure: {e}')
def connecting(name, crypto):
    colors = {'HEADER' : "\033[95m",
    'OKBLUE' : "\033[94m",
    'RED' : "\033[91m",
    'OKYELLOW' : "\033[93m",
    'GREEN' : "\033[92m",
    'LIGHTBLUE' : "\033[96m",
    'WARNING' : "\033[93m",
    'FAIL' : "\033[91m",
    'ENDC' : "\033[0m",
    'BOLD' : "\033[1m",
    'UNDERLINE' : "\033[4m" }
    crypto.readkey()
    ip = input('Insert ip: ') #192.168.100.22
    try:
        port = int(input('insert port: ')) #port = 5555
    except:
        return
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        start_new_thread(Print_response, (s, crypto))
        out = input()
        out = hashlib.sha1(out.encode('utf-8')).hexdigest()
        out = crypto.encrypt(out.encode('utf-8'))
        s.send(out)
        while True:
            out = '\n'+name + ': '+input()+'\n'
            print(colors['WARNING']+ out.split(': ')[0]+ ': '+colors['GREEN']+out.split(': ')[1])
            out = crypto.encrypt(out.encode('utf-8'))
            s.send(out)
    except Exception as e:
        print(e)
        pass

def Main():
    name = input('Insert Name: ')
    crypto = client_crypto()
    if os.path.isfile('Key'):
        while True:
            connecting(name, crypto)
        s.close()
    else:
        print('No key provided')
if __name__ == '__main__':
    Main()
