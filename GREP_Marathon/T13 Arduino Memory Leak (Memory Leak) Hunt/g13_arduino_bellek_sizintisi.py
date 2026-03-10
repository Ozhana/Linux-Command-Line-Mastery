import random

with open("g13_memory_usage.log", "w") as f:
    free_ram = 2048
    for i in range(1000):
        # Bellek yavaş yavaş azalıyor (Sızıntı simülasyonu)
        free_ram -= random.choice([0, 0, 1, 2]) 
        f.write(f"Cycle_{i:03d} - Free RAM: {free_ram} bytes\n")

print("g13_memory_usage.log oluşturuldu.")
