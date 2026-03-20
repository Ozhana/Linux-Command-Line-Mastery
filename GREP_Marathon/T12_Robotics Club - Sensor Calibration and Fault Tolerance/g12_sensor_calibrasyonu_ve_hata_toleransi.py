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

with open("g12_sensor_raw.log", "w") as f:
    for i in range(500):
        # Gerçekçi değerler (çoğunlukla 20-50 cm arası)
        dist = round(random.uniform(20.0, 50.0), 2)
        # Arada bir aşırı uç değerler (Hatalı)
        if random.random() < 0.1:
            dist = random.choice([0.5, 999.9, -1.0, 550.2])
        f.write(f"14:05:{i:02d},{dist}\n")

print("g12_sensor_raw.log oluşturuldu.")
