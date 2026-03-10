import random

users = [f"USER_{i:02d}" for i in range(10, 30)]
actions = ["ENTRY", "EXIT"]
results = ["SUCCESS", "SUCCESS", "SUCCESS", "FAIL"] # %25 hata ihtimali

with open("g19_access_logs.txt", "w") as f:
    for i in range(1000):
        day = "10-03-2026"
        hour = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}:{random.randint(0, 59):02d}"
        user = random.choice(users)
        action = random.choice(actions)
        res = random.choice(results)
        f.write(f"{day} {hour} | {user} | {action} | {res}\n")

print("g19_access_logs.txt oluşturuldu. Güvenlik taraması başlasın!")
