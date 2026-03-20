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

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"]
with open("g8_sales.csv", "w") as f:
    f.write("Date,Product,Qty,Price\n")
    for _ in range(300):
        date = f"2026-03-{random.randint(1,31):02d}"
        prod = random.choice(products)
        qty = random.randint(1, 5)
        # Çoğunluk düşük fiyat, azınlık yüksek fiyat (Outlier)
        price = random.choice([random.randint(50, 500), random.randint(1000, 5000)])
        f.write(f"{date},{prod},{qty},{price}\n")

print("g8_sales.csv oluşturuldu.")
