from Crypto.Cipher import AES
import base64
import os
#key = '12345678901234567890123456789012'


def Decrypt(encrypted):
    global cipher
    dec = cipher.decrypt(encrypted).decode('utf-8')
    c = dec.count('{')
    return dec[:len(dec)-c]


filename = input("filename: ")
key = input("Insert key: ")
cipher = AES.new(key)
with open(filename, mode='rb') as file:
    fileContent = file.read()
    decoded = Decrypt(fileContent)
    print(decoded)
