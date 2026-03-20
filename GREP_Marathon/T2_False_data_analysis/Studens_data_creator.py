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

cities = ["Ankara", "Istanbul", "Izmir", "ANKARA", "ankara", "Bursa"]
depts = ["Computer Eng", "Mathematics", "Physics", "COMPUTER Science", "Biology"]
names = ["Ahmet", "Mehmet", "Ayse", "Fatma", "Can", "Ece", "Zeynep"]

with open("students.csv", "w") as f:
    f.write("Name,City,Department,Grade\n")
    for i in range(150):
        f.write(f"{random.choice(names)},{random.choice(cities)},{random.choice(depts)},{random.randint(40,100)}\n")

print("students.csv oluşturuldu.")
