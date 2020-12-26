import socket
import constants

def get_ip() :
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip=s.getsockname()[0]
    s.close()
    return ip

def get_connected_users() :
    ip=get_ip()
    ip=ip.split('.')
    me=int(ip.pop(-1))
    connected=[]
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    for i in range(1,250):
        if i!=me:
            next_ip='.'.join(ip)+'.'+str(i)
            addr=(next_ip,5050)
            try :
                sock.connect(addr)
                utilities.send_msg(constants.PING_MSG,sock)
                connected.append[(next_ip,utilites.recieve_msg(sock))]
            except :
                continue

def recieve_msg(conn) :
    msg_length=conn.recv(constants.HEADER).decode(constants.FORMAT)
    if msg_length:
        msg_length=int(msg_length)
        msg=conn.recv(msg_length)
        msg=msg.decode(constants.FORMAT)
        return msg
    else :
        return ''

def send_msg(msg,conn):
    message=msg.encode(constants.FORMAT)
    length=str(len(msg)).encode(constants.FORMAT)
    length+=b' '*(constants.HEADER-len(length))
    conn.send(length)
    conn.send(message)
