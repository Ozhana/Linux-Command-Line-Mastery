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

log_levels = ["INFO", "DEBUG", "ERROR", "CRITICAL", "WARNING", "error", "Critical"]
messages = ["Connection failed", "User logged in", "Disk full", "Service started", "Timeout occurred"]

with open("system.log", "w") as f:
    for i in range(100):
        level = random.choice(log_levels)
        msg = random.choice(messages)
        f.write(f"2026-03-06 14:{random.randint(10,59)} - {level} - {msg}\n")

print("system.log FILE CREATED.")
