import socket

PORT=5050
HEADER=64
FORMAT='utf-8'
DISCONNECT_MESSAGE='bye_0x8x0_eyb'
SERVER='127.0.1.1'
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    length=str(len(msg)).encode(FORMAT)
    length+=b' '*(HEADER-len(length))
    client.send(length)
    client.send(message)
    
def start():
    connected=True
    print('[CONNECTED]...')
    while connected :
        msg=str(input('-> '))
        send(msg)
        if msg==DISCONNECT_MESSAGE:
            connected=False
    print('Disconnecting')
    client.close()
    
if __name__=='__main__':
    start()
