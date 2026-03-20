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

def generate_g27_data():
    products = ["PRO_Drill", "Hammer", "PRO_Saw", "Wrench", "PRO_Screwdriver"]
    branches = ["BRANCH_A", "BRANCH_B", "BRANCH_C"]
    
    with open("g27_sales_raw.csv", "w") as f:
        f.write("--- SALES REPORT V2.1 ---\n")
        f.write("DATE: 2026-03-13 | OPERATOR: ADMIN\n")
        for i in range(1, 1010):
            prod = random.choice(products)
            qty = random.randint(1, 10)
            price = random.randint(20, 150)
            branch = random.choice(branches)
            # Format: ID:001 | BRANCH:A | ITEM:PRO_Drill | QTY:5 | PRICE:120
            f.write(f"ID:{i:03} | BRANCH:{branch} | ITEM:{prod} | QTY:{qty} | PRICE:{price}\n")
        f.write("--- TOTAL CALCULATED ---\n")

if __name__ == "__main__":
    generate_g27_data()
    print(">>> 'g27_sales_raw.csv' 100 işlem ile üretildi. Analiz vakti Dr. Akdağ.")
