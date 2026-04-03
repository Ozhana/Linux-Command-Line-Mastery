import random

def generate_data():
    actions = ["PROJECT_COMPLETE", "REFUND", "BONUS", "WITHDRAWAL"]
    devices = ["Fedora_v43", "Windows_11", "Android_v14", "iOS_v17"]
    
    with open("g01_freelance_data.log", "w") as f:
        for i in range(1, 1010):
            uid = f"USR{random.randint(100, 999)}"
            action = random.choice(actions)
            amount = round(random.uniform(10.0, 500.0), 2)
            duration = random.randint(5, 120)
            device = random.choice(devices)
            f.write(f"{uid} {action} {amount} {duration}min {device}\n")

if __name__ == "__main__":
    generate_data()
    print("Veri dosyası 'g01_freelance_data.log' başarıyla oluşturuldu.")
