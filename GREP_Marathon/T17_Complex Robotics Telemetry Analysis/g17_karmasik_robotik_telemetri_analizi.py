import random
import time

sensors = [("DIST", "cm"), ("TEMP", "C"), ("SPEED", "m/s")]
statuses = ["ACTIVE", "IDLE", "ERROR"]

with open("g17_telemetry.log", "w") as f:
    for i in range(1000):
        t_str = f"14:{random.randint(10,59):02d}:{random.randint(10,59):02d}"
        s_type, unit = random.choice(sensors)
        status = random.choice(statuses)
        
        if s_type == "DIST":
            val = round(random.uniform(10.0, 99.0), 1)
        elif s_type == "TEMP":
            val = round(random.uniform(15.0, 45.0), 1)
        else:
            val = round(random.uniform(0.5, 5.0), 1)
            
        f.write(f"[{t_str}] {s_type}:{val} ({unit}) {status}\n")

print("g17_telemetry.log oluşturuldu. Veri hacmi yüksek, dikkatli süz!")
