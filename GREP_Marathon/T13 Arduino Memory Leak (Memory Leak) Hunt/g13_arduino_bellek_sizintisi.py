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

with open("g13_memory_usage.log", "w") as f:
    free_ram = 2048
    for i in range(1000):
        # Bellek yavaş yavaş azalıyor (Sızıntı simülasyonu)
        free_ram -= random.choice([0, 0, 1, 2]) 
        f.write(f"Cycle_{i:03d} - Free RAM: {free_ram} bytes\n")

print("g13_memory_usage.log oluşturuldu.")
