import socket

# CHANGE IP TO YOUR TARGET
target = "192.168.1.1" #HRE
start_port = 1
end_port = 100 #SCAN PORTS 1 - 100

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

found_open = False

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        print(f"[+] Port {port} is open ({service})")
        found_open = True
    sock.close()

if not found_open:
    print("No open ports found.")