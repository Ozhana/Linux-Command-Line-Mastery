def generate_join_data():
    # Dosya 1: Ogrenciler
    with open("ogrenciler.txt", "w") as f:
        f.write("101,Dr_Ozhan\n")
        f.write("102,Ali_K\n")
        f.write("103,Zeynep_D\n")
        f.write("104,Murat_S\n")
        f.write("105,Ayse_M\n")

    # Dosya 2: Notlar (Bazı öğrenciler eksik!)
    with open("notlar.txt", "w") as f:
        f.write("101,95\n")
        f.write("102,80\n")
        # 103'ün notu yok (Sınava girmedi)
        f.write("104,70\n")
        f.write("105,85\n")

if __name__ == "__main__":
    generate_join_data()
    print("Dosyalar 'ogrenciler.txt' ve 'notlar.txt' olarak oluşturuldu.")
