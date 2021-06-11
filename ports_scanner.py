import socket
from IPy import IP

ipadress = input("[+] Enter Target to scan :")

def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipadress, port))
        print("[+] Port "+ str(port) +" is open")
    except:
        print("[-] Port "+ str(port) +" is closed")


for i in range(75,85):
    scan_port(ipadress,i)