import socket
import threading
import utilities

PORT=5050
IP=utilities.get_ip()
ADDR=(IP,PORT)
HEADER=64
FORMAT='utf-8'
DISCONNECT_MESSAGE='bye_0x8x0_eyb'

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleclient(conn,addr):
    print(f'[NEW CONNECTED] {addr} connected')
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length)
            msg=msg.decode(FORMAT)
            if msg==DISCONNECT_MESSAGE:
                connected=False
                continue
            print(f'[NEW MESSAGE] {socket.gethostbyaddr(addr[0])} : {msg}')
    print(f'[DISCONNECTING] {socket.gethostbyaddr(addr[0])} ')
    conn.close()
    
def start():
    print(f'[STARTING] Server starting')
    server.listen()
    print(f'[LISTENING] listening at {ADDR}')
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handleclient,args=(conn,addr))
        thread.start()
        print(f'[CONNECTED] {threading.active_count()-1}')

if __name__=='__main__':
    start()        
        
