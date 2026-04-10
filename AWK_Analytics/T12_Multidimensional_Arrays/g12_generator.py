
import random

def generate_big_data():
    deps = ["Math", "IT", "HR", "Science", "Admin", "math", "it"] # Karışık case
    days = ["Pazartesi", "Sali", "Carsamba", "Persembe", "Cuma"]
    
    with open("g12_yemekhane_big.csv", "w") as f:
        f.write("Departman,Gun,Harcama\n") # Header
        for i in range(500):
            d = random.choice(deps)
            g = random.choice(days)
            # Normal harcama 20-200 arası, ama arada anomaliler var!
            if i % 50 == 0: 
                h = random.randint(-500, -1) # Negatif anomali
            elif i % 75 == 0:
                h = 5000 # Çok yüksek anomali
            else:
                h = random.randint(20, 250)
            
            f.write(f"{d},{g},{h}\n")

if __name__ == "__main__":
    generate_big_data()
    print("500 satırlık 'g12_yemekhane_big.csv' oluşturuldu. Bol şans hocam!")
