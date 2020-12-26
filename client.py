import socket
import utilities

PORT=5050
HEADER=64
FORMAT='utf-8'
DISCONNECT_MESSAGE='bye_0x8x0_eyb'
IP=utilities.get_ip()
ADDR=(IP,PORT)


def send(msg,client):
    message=msg.encode(FORMAT)
    length=str(len(msg)).encode(FORMAT)
    length+=b' '*(HEADER-len(length))
    client.send(length)
    client.send(message)
    
def chat(addr):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(addr)
    connected=True
    print('[CONNECTED]...')
    while connected :
        msg=str(input('-> '))
        send(msg,client)
        if msg==DISCONNECT_MESSAGE:
            connected=False
    print('Disconnecting')
    client.close()
    
if __name__=='__main__':
    chat(ADDR)
