import random

ips = [f"192.168.1.{i}" for i in range(1, 20)] + ["10.0.0.5", "172.16.0.100"]
ports = ["80", "443", "22", "8080", "4444", "3306"]
statuses = ["ALLOWED", "BLOCKED"]

with open("network_traffic.log", "w") as f:
    for _ in range(200):
        src = random.choice(ips)
        dst = random.choice(ips)
        port = random.choice(ports)
        status = random.choice(statuses)
        f.write(f"{src} -> {dst}:{port} [{status}]\n")

print("network_traffic.log oluşturuldu.")
