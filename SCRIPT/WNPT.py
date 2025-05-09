# wifi_scanner.py
# Educational use only - Requires monitor mode (e.g., wlan0mon)

from scapy.all import *
from scapy.layers.dot11 import Dot11Beacon, Dot11, Dot11Elt
import os

networks = {}

def callback(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11Elt].info.decode(errors="ignore")
        bssid = packet[Dot11].addr2
        if bssid not in networks:
            networks[bssid] = ssid
            print(f"[+] Found Network: SSID='{ssid}' | BSSID={bssid}")

def start_scan(interface):
    print(f"[*] Scanning for networks on interface: {interface} (Monitor Mode Required)")
    sniff(iface=interface, prn=callback, timeout=30)

if __name__ == "__main__":
    interface = input("Enter your wireless interface (e.g., wlan0mon): ")
    try:
        start_scan(interface)
    except PermissionError:
        print("[-] Permission denied. Run this script as root (sudo).")
    except Exception as e:
        print(f"[-] Error: {e}")