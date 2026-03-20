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

parts = [
    ("HC-SR04", "Sensor"), ("MPU6050", "Sensor"), ("L298N", "Motor_Driver"),
    ("SG90_Servo", "Motor"), ("Nema17", "Motor"), ("Arduino_Uno", "MCU"),
    ("LiPo_11.1V", "Battery"), ("Buzzer", "Output"), ("DC_Motor", "Motor")
]

with open("g18_inventory.txt", "w") as f:
    for i in range(200):
        name, cat = random.choice(parts)
        stock = random.randint(1, 25)
        price = round(random.uniform(5.0, 150.0), 2)
        f.write(f"{name}:{stock}:{price}:{cat}\n")

print("g18_inventory.txt oluşturuldu. Stok denetimi başlasın!")
