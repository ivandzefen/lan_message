import socket
import threading
import utilities
import constants

IP=utilities.get_ip()
ADDR=(IP,constants.PORT)
username=''

def handleclient(conn,addr,user_list,username):
    connected=True
    while connected:
        msg=utilities.recieve_msg(conn)
        if not msg:
            pass
        elif msg[0]==constants.PING_MSG:
            utilities.send_msg(username,conn)
        elif msg[0]==constants.DISCONNECT_MESSAGE:
            connected=False
        else :
            if addr not in user_list:
                user_list[addr]=[msg[1],[]]
            print(f'[NEW MESSAGE] {user_list[addr][0]} : {msg[0]}')
            if not user_list[addr][2] :
                user_list[addr][1].append(msg[0])
    print(f'[DISCONNECTING] {socket.gethostbyaddr(addr[0])} ')
    conn.close()

def start(user_list,done):

    username=str(input('please enter a username : '))
    utilities.get_connected_users(user_list)
    done=True
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    #print(f'[STARTING] Server starting')
    server.listen()
    #print(f'[LISTENING] listening at {ADDR}')

    change=user_list[constants.CHANGE_BIT]
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handleclient,args=(conn,addr,username,user_list))
        thread.start()
        #print(f'[CONNECTED] {threading.active_count()-1}')
        if change!=user_list[constants.CHANGE_BIT] :
            change=user_list[constants.CHANGE_BIT]
            user_list={}
            user_list[constants.CHANGE_BIT]=change
            utilities.get_connected_users(user_list)

if __name__=='__main__':
    start()
