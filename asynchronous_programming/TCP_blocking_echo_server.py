import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 5566))
s.listen(10)

while True:
    conn, addr = s.accept()
    msg = conn.recv(1024)
    conn.send(msg)
