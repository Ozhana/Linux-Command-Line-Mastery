import random

with open("g15_wifi_packets.log", "w") as f:
    for i in range(1, 1010):
        # %10 ihtimalle paket kaybolsun (yazılmasın)
        if random.random() > 0.1:
            f.write(f"ID:{i:03d}, RSSI:-{random.randint(40, 80)}dBm, Status:OK\n")

print("g15_wifi_packets.log oluşturuldu.")
