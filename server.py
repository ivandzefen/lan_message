import socket
import threading
import utilities
import constants

IP=utilities.get_ip()
ADDR=(IP,constants.PORT)
username=str(input('please enter a username : '))

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handleclient(conn,addr):
    print(f'[NEW CONNECTED] {addr} connected')
    connected=True
    while connected:
        msg=utilities.recieve_msg(conn)
        if not msg:
            pass
        elif msg==constants.PING_MSG:
            utilities.send_msg(username,conn)
        elif msg==constants.DISCONNECT_MESSAGE:
            connected=False
        else :
            print(f'[NEW MESSAGE] {addr} : {msg}')
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
