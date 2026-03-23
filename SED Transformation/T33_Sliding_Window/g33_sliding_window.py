import random

def generate_g33_data():
    users = ["admin", "guest", "db_user", "unknown"]
    outcomes = ["SUCCESS", "FAILURE", "FAILURE"] # Failure ihtimali daha yüksek
    
    with open("g33_network.log", "w") as f:
        for i in range(1, 410):
            user = random.choice(users)
            outcome = random.choice(outcomes)
            f.write(f"ATTEMPT: {user}\n")
            f.write(f"RESULT: {outcome}\n")
            # Bazen araya bağımsız bir sistem mesajı girsin (bozucu etki)
            if i % 5 == 0:
                f.write("SYSTEM: Periodic Check OK\n")

if __name__ == "__main__":
    generate_g33_data()
    print(">>> 'g33_network.log' (80+ satır) üretildi.")
