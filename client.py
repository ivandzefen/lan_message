import socket
import utilities
import constants

IP=utilities.get_ip()
ADDR=(IP,constants.PORT)


def chat(addr):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(addr)
    connected=True
    print('[CONNECTED]...')
    while connected :
        msg=str(input('-> '))
        utilities.send_msg(msg,client)
        if msg==constants.DISCONNECT_MESSAGE :
            connected=False
        if msg==constants.PING_MSG :
            print(utilities.recieve_msg(client))
    print('Disconnecting')
    client.close()

if __name__=='__main__':
    chat(ADDR)
