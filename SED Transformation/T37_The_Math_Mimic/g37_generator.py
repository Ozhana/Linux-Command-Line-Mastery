import random

def generate_g37_data():
    with open("g37_inventory.txt", "w") as f:
        for i in range(500, 6200):
            stock = random.randint(0, 100)
            reorder = "NO"
            f.write(f"PROD_ID: {i} | STOCK: {stock} | REORDER: {reorder}\n")

if __name__ == "__main__":
    generate_g37_data()
    print(">>> 'g37_inventory.txt' hazır. Envanter yönetimi başlıyor!")
