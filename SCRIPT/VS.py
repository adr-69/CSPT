import socket

#CHANGE IP TO WANT SCAN VULNERABILITY 
target = "192.168.1.1" 
start_port = 1
end_port = 100

vuln_ports = {
    21: "FTP - Often vulnerable to anonymous login",
    22: "SSH - Weak passwords or outdated versions",
    23: "Telnet - Unencrypted, insecure",
    80: "HTTP - Might be running outdated web server",
    139: "NetBIOS - Can be exploited in some Windows configs",
    445: "SMB - EternalBlue (WannaCry exploit)",
    3306: "MySQL - Might allow remote login with weak creds"
}

print(f"\nScanning {target} for vulnerable services...\n")
found_vuln = False

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))
    if result == 0:
        service = vuln_ports.get(port, None)
        if service:
            print(f"[!] Vulnerable Service Detected on port {port}: {service}")
            found_vuln = True
        else:
            print(f"[+] Port {port} is open (no known vuln in list)")
    sock.close()

if not found_vuln:
    print("\nNo known vulnerable services found (based on static list).")
    
    
    