import socket
from IPy import IP

#string colors
OKBLUE = '\033[94m'
ENDC = '\033[0m'
BOLD = '\033[1m'
WARNING = '\033[93m'
FAIL = '\033[91m'

def scan(target):
    converted_ip = checkIP(target)
    print("\n"+ "[scanning target] "+ BOLD+OKBLUE+ str(target)+ENDC+ENDC)
    for port in range(1,100):
        scan_port(converted_ip,port)

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

targets = input("[+] Enter Target(s) to scan ( for mutiples targets, split with ',' ): ")
 
if ',' in targets:
    for ipadress in targets.split(','):
        scan(ipadress)
else:
    scan(targets)