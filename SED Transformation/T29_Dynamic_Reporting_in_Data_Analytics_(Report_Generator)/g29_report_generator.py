import random

def generate_g29_data():
    statuses = ["SYSTEM_OK", "MAINTENANCE", "HIGH_LOAD"]
    errors = ["DB_Timeout_High", "Auth_Fail_Low", "Network_Lag_High", "Disk_Full_Critical"]
    
    with open("g29_system.log", "w") as f:
        current_status = statuses[0]
        for i in range(1, 51):
            if i % 10 == 0:
                current_status = random.choice(statuses)
                f.write(f"STATUS: {current_status}\n")
            
            err = random.choice(errors)
            f.write(f"ERROR: {err}\n")

if __name__ == "__main__":
    generate_g29_data()
    print(">>> 'g29_system.log' üretildi. Çekmece (Hold Space) kullanımına hazır olun!")
