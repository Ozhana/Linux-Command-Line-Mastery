import random

def generate_student_data():
    students = ["Ali_K", "Veli_Y", "Ayse_M", "Fatma_T", "Can_E", "Zeynep_D", "Murat_S", "Beren_A"]
    with open("g03_student_scores.csv", "w") as f:
        # Header: Name,Math,Physics,Robotics
        f.write("Name,Math,Physics,Robotics\n")
        for name in students:
            m = random.randint(30, 100)
            p = random.randint(30, 100)
            r = random.randint(30, 100)
            f.write(f"{name},{m},{p},{r}\n")

if __name__ == "__main__":
    generate_student_data()
    print("'g03_student_scores.csv' oluşturuldu. Analize başla!")
