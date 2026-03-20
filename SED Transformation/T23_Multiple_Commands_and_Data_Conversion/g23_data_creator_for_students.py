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
STUDENT DATA GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates fake student data for terminal-based 
data manipulation training.
"""

import random

def generate_g23_data():
    statuses = ["PASS", "FAIL", "N/A"]
    with open("g23_students.csv", "w") as f:
        for i in range(1, 510):
            name = f"student_{i:02}"
            grade = random.randint(30, 100)
            status = random.choice(statuses)
            absence = random.randint(0, 15)
            # Virgüllü CSV formatı
            f.write(f"{name},{grade},{status},{absence}\n")

if __name__ == "__main__":
    generate_g23_data()
    print(">>> 'g23_students.csv' (50 öğrenci) üretildi. Başarılar Dr. Akdağ.")
