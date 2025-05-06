import ipaddress
import subprocess
import socket
from concurrent.futures import ThreadPoolExecutor

#CHANGE IP TO YOUR TARGET
network = ipaddress.ip_network('192.168.8.1/24', strict=False)

def ping(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', '-W', '1', str(ip)],
                                         stderr=subprocess.DEVNULL)
        try:
            hostname = socket.gethostbyaddr(str(ip))[0]
        except socket.herror:
            hostname = "Unknown"
        print(f"[+] Active: {ip} ({hostname})")
    except subprocess.CalledProcessError:
        pass
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(ping, network.hosts())
    