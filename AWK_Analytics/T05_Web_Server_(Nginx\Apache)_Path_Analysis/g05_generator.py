import random

def generate_web_logs():
    paths = ["/home", "/urun/laptop", "/urun/telefon", "/kategori/kitap", "/api/v1/login", "/about"]
    params = ["?id=123", "?ref=google", "?sort=asc", ""]
    codes = ["200", "200", "200", "404", "500", "200"] # 200 ağırlıklı
    
    with open("g05_web_access.log", "w") as f:
        for _ in range(3000):
            p = random.choice(paths) + random.choice(params)
            code = random.choice(codes)
            ip = f"192.168.1.{random.randint(10,99)}"
            # Format: IP [ZAMAN] "GET /path HTTP/1.1" STATUS_CODE
            f.write(f'{ip} [04/Apr/2026:12:00:00] "GET {p} HTTP/1.1" {code}\n')

if __name__ == "__main__":
    generate_web_logs()
    print("'g05_web_access.log' üretildi.")
