import itertools
import string

target_password = "ab"  # The password we want to guess
characters = string.ascii_lowercase + string.digits

found = False

for length in range(1, 6):  # Adjust max length for deeper cracking
    for guess in itertools.product(characters, repeat=length):
        attempt = ''.join(guess)
        print(f"Trying: {attempt}")
        if attempt == target_password:
            print(f"[+] Password found: {attempt}")
            found = True
            break
    if found:
        break

if not found:
    print("[-] Password not cracked.")