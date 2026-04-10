def generate_security_data():
    with open("g11_security_logs.csv", "w") as f:
        f.write("ozhan,2,1,0\n")
        f.write("ali,12,5,3\n")
        f.write("ayse,1,0,0\n")
        f.write("mehmet,8,2,1\n")

if __name__ == "__main__":
    generate_security_data()
    print("Güvenlik logları hazır!")
