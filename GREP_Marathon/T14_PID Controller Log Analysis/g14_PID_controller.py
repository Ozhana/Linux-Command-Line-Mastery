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

with open("g14_pid_debug.log", "w") as f:
    f.write("Time,Target,Current,Error\n")
    for i in range(300):
        target = 500
        # Normalde hata küçük, ama sonda robot pistten çıkıyor
        if i > 250:
            current = target + random.randint(50, 100)
        else:
            current = target + random.randint(-5, 5)
        error = current - target
        f.write(f"10:00:{i:03d},{target},{current},{error}\n")

print("g14_pid_debug.log oluşturuldu.")
