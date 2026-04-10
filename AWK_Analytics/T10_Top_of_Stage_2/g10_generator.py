def generate_system_data():
    # Dosya 1: users.txt (username:full_name:department)
    with open("users.txt", "w") as f:
        f.write("ozhan:Dr_Ozhan:Math\n")
        f.write("ali:Ali_K:IT\n")
        f.write("ayse:Ayse_M:Math\n")
        f.write("mehmet:Mehmet_R:IT\n")
        f.write("zeynep:Zeynep_D:HR\n")

    # Dosya 2: logins.txt (username:login_count:last_ip)
    with open("logins.txt", "w") as f:
        f.write("ozhan:5:192.168.1.50\n")
        f.write("ali:15:10.0.0.1\n") # IT değil ama yoğun login (Şüpheli)
        f.write("mehmet:2:172.16.0.5\n")
        # Ayse ve Zeynep login olmamış (Pasif)
        
if __name__ == "__main__":
    generate_system_data()
    print("Sistem dosyaları hazır!")
