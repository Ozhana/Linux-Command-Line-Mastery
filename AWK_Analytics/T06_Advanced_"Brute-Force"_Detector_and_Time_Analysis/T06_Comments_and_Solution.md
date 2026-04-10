# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 7.5/10 | ***### Zorluk duzeyi:*** 7.5/10|
| SCENARIO: On the Fedora server secure.log there is a very sneaky attacker in his file. Not only does it try the wrong password, it does it in very short periods of time (in seconds). It's just your job Failed not finding what happened; in the same second detecting “hyper-active” attackers conducting multiple attempts.| SENARYO: Fedora sunucundaki secure.log dosyasında çok sinsi bir saldırgan var. Sadece yanlış şifre denemekle kalmıyor, bunu çok kısa sürelerde (saniyeler içinde) yapıyor. Senin görevin, sadece Failed olanları bulmak değil; aynı saniye içinde birden fazla deneme yapan "hiper-aktif" saldırganları tespit etmek. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Time Based Grouping: Each "Second" ( using an array$1) how many in it Failed count as tried (saldiri_sayisi[$1]++).<br><br>2. IP and User Matching: Combine which IP is targeting which user as a string every second and keep it in the array (hedef[$1] = $9 " -> " $11).<br><br>3. Dynamic Threshold (Threshold): END set up a loop on your block. If in a second 3 or more if there is a failed attempt, do it "CRITICAL: Brute-Force Detection!" report by title.<br><br>4. Mathematical Bonus: Calculate the “Average Attempts Per Attacker” rate by dividing the total number of attacks by the total number of unique (unique) attacker IPs.<br><br>5. Released Clean: Give the output in order of time (1st column) (You know, the one coy in Fedora sort using the command outside: \| sort -t' ' -k1). | 1. Zaman Bazlı Gruplama: Bir dizi kullanarak her bir "Saniye" ($1) içinde kaç tane Failed denemesi yapıldığını say (saldiri_sayisi[$1]++).<br><br>2. IP ve Kullanıcı Eşleşmesi: Her bir saniyede hangi IP'nin hangi kullanıcıyı hedeflediğini bir string olarak birleştirip dizide tut (hedef[$1] = $9 " -> " $11).<br><br>3. Dinamik Eşik (Threshold): END bloğunda bir döngü kur. Eğer bir saniye içinde 3 veya daha fazla başarısız deneme varsa, bunu "KRITIK: Brute-Force Tespiti!" başlığıyla raporla.<br><br>4. Matematiksel Bonus: Toplam saldırı sayısını, toplam eşsiz (unique) saldırgan IP sayısına bölerek "Saldırgan Başına Ortalama Deneme" oranını hesapla.<br><br>5. Temiz Çıktı: Çıktıyı zamana göre (1. sütun) sıralı ver (Hani şu Fedora'da nazlanan sort komutunu dışarıda kullanarak: \| sort -t' ' -k1). |
| Golden Information: | Altin Bilgi: |
| If you try to access an array element that is not in the AWK, it will not give an error; make it an empty string ("") or 0 he accepts it as such and creates that key in the array at that moment (Beware of knee swelling!). | AWK'da olmayan bir dizi elemanına erişmeye çalışırsan hata vermez; onu boş bir string ("") veya 0 olarak kabul eder ve o an o anahtarı dizide oluşturur (Dizi şişmesine dikkat!). |
| Analytical Question: | Analitik Soru: |
| Whether there is a key (key) inside an array in AWK if (anahtar in dizi) we can check it like this. Well, directly without doing this check dizi[anahtar] what does AWK do if we write it? | AWK'da bir dizinin içinde bir anahtarın (key) olup olmadığını if (anahtar in dizi) şeklinde kontrol edebiliriz. Peki bu kontrolü yapmadan direkt dizi[anahtar] yazarsak AWK ne yapar? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN {
    printf "%-28s | %-10s | %-20s | %-10s \n", "DURUM", "SANIYE", "HEDEF (USER->IP)", "ATAK";
    print "--------------------------------------------------------------------------------"
    toplam_saldiri = 0;
}

{
    # $1: Saniye, $2: Orijinal Zaman, $8: User, $10: IP (to_second eklediğimiz için sütunlar kaydı)
    # Saniyeyi anahtar yaparak her saniyedeki veriyi biriktirelim
    saldiri_sayisi[$1]++;
    toplam_saldiri++;
    
    # Zaman bilgisini de bir dizide saklayalım ki END bloğunda basalım
    zaman_etiketi[$1] = $2;
    hedef_bilgisi[$1] = $8 " -> " $10;
    
    # UNIQUE IP SAYMA (İşte aradığın çözüm):
    ips[$10] = 1; 
}

END {
    unique_ip_sayisi = 0;
    for (i in ips) { unique_ip_sayisi++ }

    for (k in saldiri_sayisi) {
        status = (saldiri_sayisi[k] >= 3) ? "KRITIK: Brute-Force!" : "NORMAL";
        printf "%-28s | %-10s | %-20s | %-10d \n", status, zaman_etiketi[k], hedef_bilgisi[k], saldiri_sayisi[k];
    }

    print "--------------------------------------------------------------------------------"
    print "Toplam Saldırı Sayısı       : " toplam_saldiri;
    print "Eşsiz (Unique) Saldırgan IP : " unique_ip_sayisi;
    
    # Matematikçi Bonus:
    if (unique_ip_sayisi > 0) {
        printf "Saldırgan Başına Ortalama   : %.2f\n", toplam_saldiri / unique_ip_sayisi;
    }
}
```
