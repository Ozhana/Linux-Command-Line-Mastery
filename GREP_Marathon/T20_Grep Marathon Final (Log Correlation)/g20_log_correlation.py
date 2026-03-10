import random

# Aynı zaman diliminde iki farklı log üretelim
with open("g20_sensor.log", "w") as f1, open("g20_system.log", "w") as f2:
    for i in range(1000):
        hour = f"14:{random.randint(10,59):02d}:{random.randint(10,59):02d}"
        temp = round(random.uniform(20.0, 50.0), 1)
        f1.write(f"[{hour}] TEMP:{temp}C\n")
        
        # Sadece bazı saatlerde kritik hata olsun
        if random.random() < 0.2:
            f2.write(f"[{hour}] SYSTEM_STATUS: CRITICAL_ERROR\n")
        else:
            f2.write(f"[{hour}] SYSTEM_STATUS: OK\n")

print("Loglar hazır! Bakalım hatanın kaynağını bulabilecek misin?")
