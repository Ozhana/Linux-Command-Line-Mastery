import random

log_levels = ["INFO", "DEBUG", "ERROR", "CRITICAL", "WARNING", "error", "Critical"]
messages = ["Connection failed", "User logged in", "Disk full", "Service started", "Timeout occurred"]

with open("system.log", "w") as f:
    for i in range(100):
        level = random.choice(log_levels)
        msg = random.choice(messages)
        f.write(f"2026-03-06 14:{random.randint(10,59)} - {level} - {msg}\n")

print("system.log FILE CREATED.")
