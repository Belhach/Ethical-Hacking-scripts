import socket
from IPy import IP

def checkIP(ip):
    try:
        IP(ip)
        return ip
    except ValueError :
        return socket.gethostbyname(ip)    

def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipadress, port))
        print("[+] Port "+ str(port) +" is open")
    except:
        print("[-] Port "+ str(port) +" is closed")

ipadress = input("[+] Enter Target to scan :")
converted_ip = checkIP(ipadress)

for i in range(75,85):
    scan_port(converted_ip,i)