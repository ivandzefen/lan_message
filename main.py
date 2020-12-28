import socket
import utilities
import constants
import client
import server
import threading
import time

def begin():
    user_list={}
    checkvalues={'update_table':False,'updating':True}
    done=False
    print(user_list)
    s_thread=threading.Thread(target=server.start,args=(user_list,checkvalues))
    s_thread.start()
    while True :
        while checkvalues['updating']:
            print('waiting')
            time.sleep(10)
        list=[]
        print('here')
        for i in user_list :
            if i!=constants.CHANGE_BIT:
                list.append(i)
        if  not len(list) :
            printf('no connected users retrying')
            time.sleep(10)
            continue
        print('ONLINE')
        for i in range(len(list)):
            print(f'{i+1} : {user_list[list[i]][0]}')
        chat=0
        while not chat:
            try :
                chat=int(input('select a user whit whom you want to chat'))
                if (chat-1) not in range(len(list)) :
                    print('select a valid user')
                    chat=0
            except :
                print('select a valid user')
        chat=chat-1
        inchat=True
        ip=list[chat]
        name=user_list[ip][0]
        user_list[ip][2]=1
        print(f'chatting with {name} enter EXIT to quit this chat')
        while inchat :
            for i in range(len(user_list[ip][1])):
                print(f'{name} : {user_list[ip][1].pop(0)}')
            msg=str(input('->'))
            if msg=='EXIT' :
                inchat=False
                user_list[ip][2]=0
                checkvalues['update_table']=True
                checkvalues['updating']=True
                continue
            utilities.send_msg(msg,ip,name)

if __name__=='__main__' :
    begin()
