# credential_stuffing_sim.py
# Educational purpose only

# Simulated valid credentials in a database
valid_credentials = {
    "user1@example.com": "password123",
    "admin@example.com": "admin2025",
    "test@demo.com": "qwerty123"
}

# Stolen credentials (from a breached list)
stolen_creds = [
    ("user1@example.com", "password123"),  # valid
    ("user2@example.com", "123456"),       # invalid
    ("admin@example.com", "wrongpass"),    # invalid
    ("admin@example.com", "admin2025"),    # valid
    ("test@demo.com", "qwerty123"),        # valid
    ("unknown@fake.com", "nopass"),        # invalid
]

def credential_stuffing_attack(stolen):
    print("\n[+] Starting Credential Stuffing Simulation...\n")
    for email, password in stolen:
        print(f"[*] Trying {email}:{password}...", end=' ')
        if valid_credentials.get(email) == password:
            print("[SUCCESS]")
        else:
            print("[FAILED]")
    print("\n[+] Simulation Complete.")

if __name__ == "__main__":
    credential_stuffing_attack(stolen_creds)