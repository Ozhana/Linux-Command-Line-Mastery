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

def generate_binary():
    return "".join(random.choice(["0", "1"]) for _ in range(8))

with open("g16_hardware.log", "w") as f:
    for i in range(1000):
        sensor_id = f"ID_{random.randint(10, 15):03d}"
        data = generate_binary()
        # %30 ihtimalle checksum hatası (ERR) ekleyelim
        status = "OK" if random.random() > 0.3 else "ERR"
        f.write(f"{sensor_id}: [{data}] {status}\n")

print("g16_hardware.log dosyası oluşturuldu. Analize başlayabilirsin!")
