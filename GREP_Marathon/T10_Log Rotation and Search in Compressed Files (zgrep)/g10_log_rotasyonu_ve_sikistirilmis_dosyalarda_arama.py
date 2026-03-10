import random
import os

filename = "g10_old_server_logs.txt"
with open(filename, "w") as f:
    for i in range(1000):
        level = random.choice(["INFO", "WARN", "ERROR", "CRITICAL","SUCCESS"])
        msg = f"Event_{i:03d} occurance"
        f.write(f"2025-12-31 {random.randint(10,23)}:00:00 [{level}] {msg}\n")

# Dosyayı sıkıştıralım (Linux gzip komutunu çağıralım)
os.system(f"gzip -f {filename}")
print(f"{filename}.gz oluşturuldu.")
