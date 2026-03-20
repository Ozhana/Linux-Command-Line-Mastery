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
SALES REPORT GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates sales report for terminal-based 
data manipulation training.
"""

import random

def generate_g24_data():
    customers = ["ali_yilmaz", "ayse_nur", "dr_ozhan", "mehmet_can", "canan_su"]
    products = ["PROD-744", "PROD-102", "PROD-993", "PROD-552"]
    
    with open("g24_sales.log", "w") as f:
        for i in range(1, 610):
            cust = random.choice(customers)
            prod = random.choice(products)
            price = random.randint(50, 2000)
            day = random.randint(10, 28)
            month = random.randint(10, 12)
            # Karmaşık format: Müşteri | (Ürün) | GG/AA/YYYY | FiyatTL
            line = f"{cust} | ({prod}) | {day}/{month}/2025 | {price}TL\n"
            f.write(line)

if __name__ == "__main__":
    generate_g24_data()
    print(">>> 'g24_sales.log' (60 karmaşık satır) üretildi.")
