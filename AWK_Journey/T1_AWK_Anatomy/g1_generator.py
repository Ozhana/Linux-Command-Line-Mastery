import random
import datetime

# 2000 satırlık siber güvenlik log datası oluşturur
def generate_security_logs():
    actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "LOGOUT", "REBOOT_REQ", "SUDO_EXC"]
    ips = [f"192.168.1.{random.randint(1, 254)}" for _ in range(50)]
    users = ["admin", "root", "guest", "db_user", "developer", "tester"]
    
    with open("ssh_logs.txt", "w") as f:
        for i in range(2000):
            date = (datetime.datetime.now() - datetime.timedelta(minutes=i)).strftime("%Y-%m-%d %H:%M:%S")
            ip = random.choice(ips)
            user = random.choice(users)
            action = random.choice(actions)
            port = random.randint(1024, 65535)
            # Format: Tarih Saat IP Kullanıcı Eylem Port
            f.write(f"{date} {ip} {user} {action} {port}\n")

if __name__ == "__main__":
    generate_security_logs()
    print("2000 satırlık 'ssh_logs.txt' başarıyla oluşturuldu.")
