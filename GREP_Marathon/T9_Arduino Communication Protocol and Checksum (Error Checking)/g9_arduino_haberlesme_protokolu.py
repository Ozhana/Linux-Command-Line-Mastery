import random

with open("g9_arduino_serial.log", "w") as f:
    for _ in range(200):
        # Bazı paketler hatalı (END yok veya DATA 2 haneli)
        data = random.choice([str(random.randint(100, 999)), str(random.randint(10, 99))])
        checksum = hex(random.randint(0, 255))[2:].upper()
        if random.random() < 0.2:
            packet = f"START:{data}:{checksum}" # Hatalı: END yok
        else:
            packet = f"START:{data}:{checksum}:END"
        f.write(packet + "\n")

print("g9_arduino_serial.log oluşturuldu.")
