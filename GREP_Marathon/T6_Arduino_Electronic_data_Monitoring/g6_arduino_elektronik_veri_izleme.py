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
import time

with open("g6.csv", "w") as f:
    for i in range(2000):
        timestamp = time.strftime("%H:%M:%S")
        # Arada bir hatalı veri (NAN veya OVF) ekleyelim
        if random.random() < 0.1:
            val = random.choice(["NAN", "OVF"])
        else:
            val = f"T:{round(random.uniform(20.0, 35.0), 2)}"
        f.write(f"{timestamp},{val}\n")

print("g6.csv oluşturuldu.")
