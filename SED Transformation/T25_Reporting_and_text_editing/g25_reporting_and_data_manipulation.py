# -*- coding: utf-8 -*-
"""
The Mathematical Lab Bench
---------------------------
Project Author: Dr. Ozhan Akdag
Academic Role: PhD in Mathematics & PhD in Education
License: MIT License
Created: 2026

Description: Part of a comprehensive mathematical computational laboratory.
"""

"""
SECURITY LOG GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates Security logs for terminal-based 
data manipulation training.
"""

import random

def generate_g25_data():
    levels = ["Critical", "High", "Low", "Low"]
    issues = ["SQL_Injection", "Buffer_Overflow", "XSS_Vulnerability", "Weak_Password", "Open_Port"]
    
    with open("g25_security_scan.txt", "w") as f:
        f.write("--- SCAN START ---\n")
        for i in range(1, 410):
            level = random.choice(levels)
            issue = random.choice(issues)
            day = random.randint(10, 28)
            # Format: SCAN_DATE: 12/03/2026 | ID-001 | LEVEL: Critical | FINDING: SQL_Injection
            f.write(f"SCAN_DATE: {day}/03/2026 | ID-{i:03} | LEVEL: {level} | FINDING: {issue}\n")
        f.write("--- SCAN END ---\n")

if __name__ == "__main__":
    generate_g25_data()
    print(">>> 'g25_security_scan.txt' (40 rapor satırı) üretildi.")
