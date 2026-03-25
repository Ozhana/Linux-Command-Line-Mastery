import random

def generate_g38_data():
    classes = ["Math-101", "Stats-202", "Data-303"]
    names = ["Ozhan", "Akdag", "Newton", "Leibniz", "Gauss"]
    with open("g38_raw_data.txt", "w") as f:
        for _ in range(15):
            f.write(f"CLASS: {random.choice(classes)} | STUDENT: {random.choice(names)} | GRADE: {random.randint(50, 100)}\n")

if __name__ == "__main__":
    generate_g38_data()
    print(">>> 'g38_raw_data.txt' hazır. XML dönüşümü başlasın!")
