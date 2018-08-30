from Crypto.Cipher import AES
import base64
import os
import random
import string
#secret = random.randrange(10000000000000000000000000000000,99999999999999999999999999999999)
secret = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(1, 33)])
key = str(secret)
cipher = AES.new(key)

def pad(s):
    return s + ((16-len(s)%16) * '{')

def Encrypt(message):
    global cipher, key
    return cipher.encrypt(pad(message))


str = input("Message: ")
encoded = Encrypt(str)

filename = 'encrypted.bin'
with open(filename,'wb') as file:
    file.write(encoded)
    print("Encrypted as "+filename)
    print("Your key: "+key)
