import socket #socket used to communicate with other devices using TCP and UDP protocols
import termcolor #used to print statements in other colors

def scan(target, ports):
    '''Iterates through ports'''
    try:
        print(termcolor.colored((f"\n Starting scan for {target}"), ("green")))
        for port in range (1, ports):
            scan_port(target, port)
    finally:
        print(termcolor.colored((f"Listed all open ports for {target}"), ("green")))

def scan_port(ipaddress, port):
    '''Scans through the given ports'''

    try: #trying to check if port is open
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port {port}: Open")
        sock.close()
    except: #port is closed
        pass


# main
targets = input("[*] Enter IP addresses of target(s) (split them by \',\'): ")
ports = int(input("[*] Enter the number of ports you want to scan: "))

if ',' in targets: #for multiple targets
    for ip_add in targets.split(','):
        scan (ip_add.strip(' '), ports)
else: #for single target
    scan(targets, ports)