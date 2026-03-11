import random

def generate_g21_data():
    users = ["admin", "guest", "dr_ozhan", "student_22", "root", "analyst_beta"]
    ips = ["192.168.1.1", "10.0.0.15", "172.16.254.1", "127.0.0.1", "8.8.8.8"]
    actions = ["LOGIN", "LOGOUT", "FAILED_ACCESS", "UPDATE", "DELETE"]
    
    with open("g21_system_logs.txt", "w") as f:
        for i in range(1, 1510):
            user = random.choice(users)
            ip = random.choice(ips)
            action = random.choice(actions)
            # Versiyon bilgisi ve yapısal log formatı
            line = f"LOG_ID:{i:03} | USER:{user} | ACTION:{action} | IP:{ip} | STATUS:old_v1\n"
            f.write(line)
            
    print(">>> 'g21_system_logs.txt' 150 satır olarak üretildi.")
    print(">>> Dr. Akdağ, veri hazır. Analiz sırası sizde.")

if __name__ == "__main__":
    generate_g21_data()
