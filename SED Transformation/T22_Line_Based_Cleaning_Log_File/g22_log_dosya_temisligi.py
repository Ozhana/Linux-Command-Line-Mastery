"""
LOG GENERATOR ENGINE v1.0
Author: Dr. Ozhan Akdag
Description: Generates synthetic system logs for terminal-based 
data manipulation training.
"""

import random

def generate_g22_data():
    levels = ["INFO", "INFO", "INFO", "WARNING", "CRITICAL", "FAILED_ACCESS"]
    ips = ["192.168.1.45", "10.0.0.12", "172.16.0.5", "192.168.1.101"]
    
    with open("g22_security_audit.log", "w") as f:
        f.write("--- SYSTEM AUDIT START ---\n")
        f.write("Time: 2026-03-12\n\n") # Bilinçli boş satır
        for i in range(1, 1010):
            level = random.choice(levels)
            ip = random.choice(ips)
            f.write(f"ID:{i:03} | LEVEL:{level} | SOURCE_IP:{ip} | MSG:System_Check\n")
            if i % 10 == 0:
                f.write("\n") # Periyodik boş satırlar
        f.write("--- END OF LOG ---\n")
        f.write("Status: Archived\n")

if __name__ == "__main__":
    generate_g22_data()
    print(">>> 'g22_security_audit.log' üretildi. Temizlik vakti Dr. Akdağ.")
