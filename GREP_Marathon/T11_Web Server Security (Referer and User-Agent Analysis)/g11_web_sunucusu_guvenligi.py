import random

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.10"]
agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)", 
    "Python-urllib/3.10", 
    "Googlebot/2.1", 
    "Curl/7.68.0"
]
referers = ["https://google.com", "-", "https://facebook.com"]

with open("g11_web_access.log", "w") as f:
    for _ in range(300):
        ip = random.choice(ips)
        agent = random.choice(agents)
        ref = random.choice(referers)
        status = random.choice(["200", "404", "500"])
        f.write(f'{ip} [07/Mar/2026] "GET /index.html" {status} "{ref}" "{agent}"\n')

print("g11_web_access.log oluşturuldu.")
