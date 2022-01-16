import socket
import threading

HEADER = 64
PORT= 5050
SERVER= socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONECT_MSG = "disconnect"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def send(msg, conn):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    print(f"[Sending] {send_length}")
    conn.send(send_length)
    print(f"[Sending] {message}")
    conn.send(message)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        user_input = input()
        if (user_input == "p"):
            connected = False
        else:
            send(user_input, conn)
            
    send(DISCONECT_MSG, conn)
    print(f"[Disconnecting]Sending disconect message to {addr}")
    conn.close()
    print(f"[Disconect] {addr} disconected")        

def start():
    server.listen()
    print(f"[LISTENING]: Server is listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[Starting] server is starting...")
start()