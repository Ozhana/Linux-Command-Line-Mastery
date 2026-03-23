import random

def generate_g35_data():
    sensors = ["temp_01", "hum_v2", "press_x", "light_y"]
    units = ["Celsius", "Percent", "Bar", "Lux"]
    
    with open("g35_sensors.csv", "w") as f:
        for i in range(1, 41):
            h = random.randint(10, 23)
            m = random.randint(10, 59)
            s_idx = random.randint(0, 3)
            val = round(random.uniform(10.0, 99.0), 1)
            f.write(f"[{h}:{m}] - {sensors[s_idx]}: {val} ({units[s_idx]})\n")

if __name__ == "__main__":
    generate_g35_data()
    print(">>> 'g35_sensors.csv' üretildi. Grupları ayırmaya hazır olun!")
