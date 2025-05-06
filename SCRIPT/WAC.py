import requests

# Target website  #this my sample website
target_url = "https://adr-69.github.io/-/PWS.htm"  # Replace with the website you want to scan

# Common paths to scan (add more if needed)
common_paths = [
    "/", "/admin", "/login", "/dashboard", "/wp-login.php", "/config", "/.git", "/robots.txt"
]

print(f"[+] Scanning {target_url} for common endpoints...\n")

for path in common_paths:
    url = target_url + path
    try:
        response = requests.get(url, timeout=5)
        code = response.status_code
        print(f"{url} => [{code}]")

        # Show server header if found
        server = response.headers.get('Server')
        if server:
            print(f"    Server: {server}")
        x_powered = response.headers.get('X-Powered-By')
        if x_powered:
            print(f"    X-Powered-By: {x_powered}")

    except requests.exceptions.RequestException:
        print(f"{url} => [Error connecting]")

print("\n[+] Scan complete.")
