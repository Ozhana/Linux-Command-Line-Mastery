import random

def generate_network_log():
    ips = ["10.0.0.1", "10.0.0.2", "192.168.1.50", "45.33.22.11", "8.8.8.8"]
    with open("g04_network_traffic.log", "w") as f:
        for _ in range(2000): # 200 satırlık trafik
            ip = random.choice(ips)
            size = random.randint(100, 50000) # Byte
            timestamp = f"{random.randint(10,23)}:{random.randint(10,59)}"
            f.write(f"{timestamp} {ip} {size}\n")

if __name__ == "__main__":
    generate_network_log()
    print("'g04_network_traffic.log' oluşturuldu.")
