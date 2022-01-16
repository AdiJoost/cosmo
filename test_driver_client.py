import socket
import testMotorDrive as md

HEADER = 64
PORT = 5050
SERVER = "192.168.1.120"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONECT_MSG = "disconnect"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    message_length = len(message)
    send_length = str(message_length).encode(FORMAT)
    send_length += b' ' * (HEADER - send_length)
    client.send(send_length)
    client.send(message)
    
def orders():
    pass

connected = True
while connected:
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length != "":
        print(f"[Client]Message with length {msg_length} recieved:")
        msg_length = int(msg_length)
        message = client.recv(msg_length).decode(FORMAT)
        if message == DISCONECT_MSG:
            connected = False
        elif message == "q":
            print(md.rigth_forward())
        elif message == "y":
            print(md.rigth_backward())
        elif message == "a":
            print(md.rigth_stop())
        elif message == "w":
            print(md.left_forward())
        elif message == "x":
            print(md.left_backward())
        elif message == "s":
            print(md.left_stop())


print(md.clean_board())
client.close()
print("[Connection closed]")