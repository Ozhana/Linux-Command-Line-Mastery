import random
import os

"""
LOG GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates synthetic system traffic logs for terminal-based 
data manipulation training.
"""

def generate_g26_data(filename="g26_raw_traffic.log", num_entries=60):
    events = ["Login_Attempt", "File_Access", "Database_Query", "Admin_Privilege_Escalation"]
    users = ["ozhan_akdag", "guest_user", "system_root", "bot_analyst"]
    
    print(f"[*] Generating {num_entries} log entries...")
    
    try:
        with open(filename, "w") as f:
            for _ in range(num_entries):
                date = f"{random.randint(10,28)}/03/2026"
                user = random.choice(users)
                event = random.choice(events)
                score = random.randint(10, 99)
                err = random.choice([404, 500, 200, 403])
                # Format: DD/MM/YYYY | USER | EVENT | SCORE | ERR_CODE: XXX
                f.write(f"{date} | {user} | {event} | {score} | ERR_CODE: {err}\n")
        print(f"[+] Success! '{filename}' is ready for analysis.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    generate_g26_data()