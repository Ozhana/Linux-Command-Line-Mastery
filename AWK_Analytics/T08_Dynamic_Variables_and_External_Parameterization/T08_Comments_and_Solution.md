# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 6/10 | ***### Zorluk duzeyi:*** 6/10|
| SCENARIO: but will give you "flexibility" at AWK: External Variable Assignment (-v parameter).<br><br>Instead of opening the code and typing "Fedora" or "Active" each time, we want to leave the AWK script as a pattern and send the criterion you are looking for as a variable from the terminal. | SENARYO: AWK'da "esneklik" kazandıracak çok kritik bir konuya geçelim: Dışarıdan Değişken Atama (-v parametresi). <br><br>Her seferinde kodu açıp "Fedora" veya "Aktif" yazmak yerine, AWK scriptini bir kalıp olarak bırakıp, aradığın kriteri terminalden bir değişken olarak göndermek istiyoruz. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Take Two Variables: from outside when running the AWK script -v os_tipi="..." and the -v durum="..." send two variables as follows.<br><br>2. Dynamic Filtering: Fixed Delete the words "Fedora" or "Active". Instead, filter the records using these two variables coming from outside.<br><br>3. Uppercase/Lowercase Sensitivity: While filtering tolower() using the function, match whether the user writes "fedora" or "FEDORA".<br><br>4. Error Checking: If no device can be found that meets the required criteria, END on his blog "No devices found in the searched criteria!" print. | 1. Iki Değişken Al: AWK scriptini çalıştırırken dışarıdan -v os_tipi="..." ve -v durum="..." şeklinde iki değişken gönder.<br><br>2. Dinamik Filtreleme: Sabit "Fedora" veya "Aktif" kelimelerini sil. Bunların yerine dışarıdan gelen bu iki değişkeni kullanarak kayıtları süz.<br><br>3. Büyük/Küçük Harf Duyarlılığı: Filtreleme yaparken tolower() fonksiyonunu kullanarak, kullanıcı "fedora" da yazsa "FEDORA" da yazsa eşleşme sağla.<br><br>4. Hata Kontrolü: Eğer aranan kriterlere uygun hiçbir cihaz bulunamazsa, END bloğunda "Aranan kriterlerde cihaz bulunamadı!" yazdır. |
| Golden Information: | Altin Bilgi: |
| -v Parameter (Variable Assignment)<br><br>When running the AWK command -v using (variable), you can pass a value in the terminal to a variable in the AWK.<br><br>Example:<br>awk -v aranacak="Fedora" '{ if ($0 ~ aranacak) print $0 }' dosya.txt<br><br>Here aranacak it's like he's in AWK now BEGIN it can be used anywhere as defined in the block. | -v Parametresi (Değişken Atama)
AWK komutunu çalıştırırken -v (variable) kullanarak terminaldeki bir değeri AWK içindeki bir değişkene paslayabilirsin. <br><br>Örnek:<br>awk -v aranacak="Fedora" '{ if ($0 ~ aranacak) print $0 }' dosya.txt<br><br>Burada aranacak artık AWK içinde sanki BEGIN bloğunda tanımlanmış gibi her yerde kullanılabilir. |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN { 
    RS = "END_RECORD\n"; 
    FS = "\n"; 
    printf "%-10s | %-20s\n", "ID", "CIHAZ ADI";
    print "-----------------------------------";
    found_count = 0 
}
{
    # Hem logdaki veriyi hem de dışarıdan gelen değişkeni küçük harfe çekip kıyaslıyoruz
    # Böylece kullanıcı 'fedora', 'Fedora' veya 'FEDORA' yazsa da çalışır.
    if (tolower($3) ~ tolower(os_tipi) && tolower($4) ~ tolower(durumu)) {
        found_count++;
        split($1, id_arr, ": ");
        split($2, cihaz_arr, ": ");
        
        # Sadece değerleri ekrana basarken küçültüyoruz (veya olduğu gibi bırakabilirsin)
        printf "%-10s | %-20s\n", id_arr[2], tolower(cihaz_arr[2]);
    }
}
END { 
    print "-----------------------------------";
    if (found_count == 0) {
        print "Aranan kriterlerde cihaz bulunamadı!"
    } else {
        # Artık sadece Fedora değil, aranan neyse onun sayısını veriyoruz
        print "Eşleşen Toplam Cihaz Sayısı: " found_count 
    }
}
```
