import random

def generate_ssh_logs():
    ips = ["192.168.1.15", "45.77.10.12", "10.0.0.5", "185.122.3.4"]
    users = ["admin", "root", "ozhan", "guest", "testuser"]
    statuses = ["Failed", "Accepted", "Invalid user"]
    
    with open("g02_ssh_auth.log", "w") as f:
        for i in range(1, 1510):
            status = random.choices(statuses, weights=[70, 10, 20])[0]
            user = random.choice(users)
            ip = random.choice(ips)
            port = random.randint(30000, 65000)
            # Log formatı: Mar 27 14:20:01 sshd[1234]: Failed password for root from 192.168.1.15 port 45678
            f.write(f"Mar 27 14:{random.randint(10,59)}:{random.randint(10,59)} sshd[{random.randint(1000,9999)}]: "
                    f"{status} password for {user} from {ip} port {port}\n")

if __name__ == "__main__":
    generate_ssh_logs()
    print("'g02_ssh_auth.log' oluşturuldu. Analize hazır!")
