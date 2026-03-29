import random

students = ["Ali", "Ayse", "Fatma", "Mehmet", "Can", "Zeynep", "Merve", "Eren"]
with open("sinav_sonuclari.txt", "w") as f:
    f.write("Ad Matematik Fizik Kimya\n")
    for s in students:
        m = random.randint(40, 100)
        p = random.randint(40, 100)
        c = random.randint(40, 100)
        f.write(f"{s} {m} {p} {c}\n")
