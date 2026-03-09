import random

# Saldırgan IP'leri (Bazıları çok baskın)
attackers = ["192.168.1.50"] * 500 + ["10.0.0.7"] * 300 + ["172.16.5.5"] * 100
others = [f"192.168.1.{i}" for i in range(100, 110)]

with open("g5.log", "w") as f:
    for _ in range(1500):
        ip = random.choice(attackers + others)
        status = random.choice(["Failed password", "Accepted password", "Failed password"])
        f.write(f"Mar 07 00:{random.randint(10,59)}:sshd[123]: {status} for root from {ip} port 22 ssh2\n")

print("g5.log oluşturuldu.")
