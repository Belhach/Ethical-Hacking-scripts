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
    for port in range(20,30):
        scan_port(converted_ip,port)

def checkIP(ip):
    try:
        IP(ip)
        return ip
    except ValueError :
        return socket.gethostbyname(ip)    

def get_banner(s):
    return s.recv(1024)

def scan_port(ipadress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipadress, port))
        try:
            banner = get_banner(sock)
            print("[+] Port "+ str(port) +" is"+OKBLUE+" open"+ENDC+" : "+str(banner.decode().strip('\n')))
        except:
            print("[+] Port "+ str(port) +" is"+OKBLUE+" open"+ENDC)   
    except:
        print("[-] Port "+ str(port) +" is"+FAIL+" closed"+ENDC)

targets = input("[+] Enter Target(s) to scan ( for mutiples targets, split with ',' ): ")
 
if ',' in targets:
    for ipadress in targets.split(','):
        scan(ipadress)
else:
    scan(targets)