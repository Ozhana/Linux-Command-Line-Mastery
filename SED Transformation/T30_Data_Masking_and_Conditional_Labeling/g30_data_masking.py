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

import random

def generate_g30_data():
    names = ["Ali Yilmaz", "Ayse Demir", "John Doe", "Dr Ozhan", "Fatma Nur"]
    countries = ["Qatar", "Turkey", "Germany", "France", "Japan"]
    
    with open("g30_customers.csv", "w") as f:
        for i in range(1, 51):
            name = random.choice(names)
            email = f"{name.lower().replace(' ', '')}{i}@example.com"
            spend = random.randint(100, 9999)
            country = random.choice(countries)
            # Format: NAME | EMAIL | SPEND | COUNTRY
            f.write(f"{name} | {email} | {spend} | {country}\n")

if __name__ == "__main__":
    generate_g30_data()
    print(">>> 'g30_customers.csv' 50 müşteriyle üretildi. Final sınavı başlasın!")
