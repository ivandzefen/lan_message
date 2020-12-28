import socket
import constants
import subprocess

def get_ip() :
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip=s.getsockname()[0]
    s.close()
    return ip

def get_connected_users(user_list) :
    ip=get_ip()
    command=['arp','-a']
    p=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,err=p.communicate()
    del(p)
    del(command)
    if len(err) :
        print('error has occured')
        return
    output=output.decode(constants.FORMAT).split('\n')
    output.pop(-1)
    for i in range(len(output)):
        output[i]=output[i].split(' ')
        output[i]=output[i][1]
        output[i]=output[i][1:-1]
    output=set(output)
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for i in output:
        if i!=ip:
            addr=(i,5050)
            print(addr)
            try :
                sock.connect(addr)
                print('here')
                utilities.send_msg(constants.PING_MSG,sock)
                user_list[i]=[utilites.recieve_msg(sock)[0],[],0]
                sock.close()
                del(sock)
            except :
                continue
    del(output)

def recieve_msg(conn) :
    msg_head=conn.recv(constants.HEADER).decode(constants.FORMAT)
    if msg_head:
        msg_length=msg_head.split(' ')[0]
        user_name=msg_head.split(' ')[1]
        msg=conn.recv(msg_lenght)
        msg=msg.decode(constants.FORMAT)
        return (msg,user_name)
    else :
        return ''

def send_msg(msg,ip,username):
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        conn.connect((ip,constants.PORT))
    except :
        print("user might be offline")
        return
    message=msg.encode(constants.FORMAT)
    length=str(len(message)).encode(constants.FORMAT)
    length+=b' '
    length+=user.encode(constants.FORMAT)
    length+=b' '*(constants.HEADER-len(lengthd))
    disconnect=constants.DISCONNECT_MESSAGE.encode(constants.FORMAT)
    lengthd=str(len(disconnect)).encode(constants.FORMAT)
    lengthd+=b' '*(constants.HEADER-len(lengthd))
    conn.send(length)
    conn.send(message)
    conn.send(lengthd)
    conn.send(disconnect)
    conn.close()
