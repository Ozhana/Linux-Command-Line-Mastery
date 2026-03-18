import random

def generate_g31_data():
    keys = ["DB_ADMIN", "WEB_SERVER", "FIREWALL", "AUTH_MOD"]
    values = ["Connection_Lost", "Login_Success", "CRITICAL_Overload", "Buffer_Warning"]
    noises = ["IGNORE_DATA_999", "TRASH_TEMP_FILE", "DUMMY_LOG_123", "SYSTEM_IDLE"]
    
    with open("g31_obfuscated.log", "w") as f:
        for i in range(1, 41):
            # 1. Her blok başına rastgele gürültü ekle
            if random.random() > 0.3:
                f.write(f"{random.choice(noises)}\n")
            
            # 2. Asıl KEY satırı
            key = random.choice(keys)
            f.write(f"KEY: {key}\n")
            
            # 3. KEY ve VALUE arasına rastgele gürültü ekle (En kritik yer!)
            for _ in range(random.randint(1, 3)):
                f.write(f"{random.choice(noises)}\n")
            
            # 4. Asıl VALUE satırı
            val = random.choice(values)
            f.write(f"VALUE: {val}\n")
            
            # 5. Blok sonuna rastgele gürültü ekle
            if random.random() > 0.3:
                f.write(f"{random.choice(noises)}\n")

if __name__ == "__main__":
    generate_g26_data = generate_g31_data # İsim düzeltmesi
    generate_g31_data()
    print(">>> 'g31_obfuscated.log' gürültülü (noisy) şekilde üretildi.")
