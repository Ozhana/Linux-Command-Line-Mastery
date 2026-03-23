import random

def generate_g36_data():
    statuses = ["APPROVED", "PENDING", "SUSPICIOUS"]
    with open("g36_transactions.log", "w") as f:
        for i in range(100, 140):
            status = random.choice(statuses)
            amt = random.randint(100, 9999)
            f.write(f"ID: {i} - STATUS: {status} - AMT: {amt}\n")

if __name__ == "__main__":
    generate_g36_data()
    print(">>> 'g36_transactions.log' üretildi. Filtreleme başlasın!")
