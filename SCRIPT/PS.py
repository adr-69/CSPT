import socket

# CHANGE IP TO YOUR TARGET
target = "192.168.8.1" #Here 
start_port = 1
end_port = 100 #SCAN OPEN PORTS 1 - 100

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

found_open = False

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[+] Port {port} is open")
        found_open = True
    sock.close()

if not found_open:
    print("No open ports found.")