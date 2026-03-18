"""
SCURITY GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates synthetic system logs for terminal-based 
data manipulation training.
"""

import random

def generate_g26_data():
    events = ["Login_Attempt", "File_Access", "Database_Query", "Admin_Privilege_Escalation"]
    users = ["ozhan_akdag", "guest_user", "system_root", "bot_analyst"]
    
    with open("g26_raw_traffic.log", "w") as f:
        for i in range(1, 610):
            date = f"{random.randint(10,28)}/03/2026"
            user = random.choice(users)
            event = random.choice(events)
            score = random.randint(10, 99)
            err = random.choice([404, 500, 200, 403])
            # Ham Format: 12/03/2026 | ozhan_akdag | Login_Attempt | 85 | ERR_CODE: 404
            f.write(f"{date} | {user} | {event} | {score} | ERR_CODE: {err}\n")

if __name__ == "__main__":
    generate_g26_data()
    print(">>> 'g26_raw_traffic.log' 610 satır olarak üretildi. Analiz başlasın!")
