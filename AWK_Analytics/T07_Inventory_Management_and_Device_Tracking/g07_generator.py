import random

def generate_inventory():
    devices = ["Surface_Pro_9", "Dell_XPS", "ThinkPad", "MacBook_Air", "Raspberry_Pi_5"]
    oss = ["Fedora_43", "Windows_11", "macOS_15", "Ubuntu_24.04"]
    statuses = ["Aktif", "Tamirde", "Kayip"]
    
    with open("g03_inventory.txt", "w") as f:
        for i in range(1, 210):
            f.write(f"ID: {1000+i}\n")
            f.write(f"Cihaz: {random.choice(devices)}\n")
            f.write(f"OS: {random.choice(oss)}\n")
            f.write(f"Durum: {random.choice(statuses)}\n")
            f.write("END_RECORD\n")

if __name__ == "__main__":
    generate_inventory()
    print("'g03_inventory.txt' (Blok yapılı) oluşturuldu.")
