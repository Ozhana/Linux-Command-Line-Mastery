import random
import time

def generate_secure_logs():
    ips = ["192.168.1.10", "45.33.22.11", "10.0.0.5"]
    users = ["root", "admin", "ozhan"]
    
    with open("g06_secure_scan.log", "w") as f:
        # Normal girişler ve sinsi saldırılar karışık
        for i in range(2000):
            timestamp = time.strftime("%H:%M:%S", time.gmtime(1712217600 + random.randint(0, 3600)))
            ip = random.choice(ips)
            user = random.choice(users)
            # Rastgele bir saniye içinde 3-4 saldırı ekleyelim (Brute force simülasyonu)
            if i % 20 == 0:
                ts_fixed = f"12:00:{random.randint(10,59):02d}"
                for _ in range(3):
                    f.write(f"{ts_fixed} sshd: Failed password for {user} from {ip}\n")
            else:
                f.write(f"{timestamp} sshd: Failed password for {user} from {ip}\n")

if __name__ == "__main__":
    generate_secure_logs()
    print("'g06_secure_scan.log' oluşturuldu.")
