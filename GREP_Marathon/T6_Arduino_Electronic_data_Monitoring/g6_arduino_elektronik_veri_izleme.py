import random
import time

with open("g6.csv", "w") as f:
    for i in range(2000):
        timestamp = time.strftime("%H:%M:%S")
        # Arada bir hatalı veri (NAN veya OVF) ekleyelim
        if random.random() < 0.1:
            val = random.choice(["NAN", "OVF"])
        else:
            val = f"T:{round(random.uniform(20.0, 35.0), 2)}"
        f.write(f"{timestamp},{val}\n")

print("g6.csv oluşturuldu.")
