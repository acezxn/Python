infect(filestoinfect) #Infect
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = -11
Origin = input('Enter encrypted message:')
# plaintext = Origin[::-1]
plaintext = Origin


# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
    else: ciphertext += c

# print (plaintext)
print (ciphertext)
# print (plaintext2)
