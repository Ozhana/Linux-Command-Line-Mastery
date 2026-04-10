# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: Now that we've figured out the functions, we're into the "deepest" waters of AWK, that is Multidimensional Arrayswe enter. In fact, AWK technically simulates these by combining a single "key", but it is very powerful to use.<br><br>We will track the cafeteria expenses of staff in different departments of the school (Math, IT, HR) on different days (Monday, Tuesday...). | SENARYO: Fonksiyonları çözdüğümüze göre, artık AWK'nın en "derin" sularına, yani Çok Boyutlu Dizilere giriyoruz. Aslında AWK teknik olarak bunları tek bir "key" birleştirmesiyle simüle eder ama kullanımı çok güçlüdür.<br><br>Okulun farklı departmanlarındaki (Math, IT, HR) personelin, farklı günlerdeki (Pazartesi, Salı...) yemekhane harcamalarını takip edeceğiz. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Cleaning: Processing negative expenses and "excessive" anomalies over 1000 TL (Log or late).<br><br>2. Normalization: Department names toupper() equate with so that "math" and "Math" are added together on the same line.<br><br>3. Multidimensional Array: harcama[dep, gun] += $3 use structure.<br><br>4. Mathematical Control: Completely calculate Row and Column totals.<br><br>5. Bonus (Wrap Trial): If the department name is longer than 5 characters, press only the first 5 characters in the table with a dot next to it (Ex: Scien.). | 1. Temizlik: Negatif harcamaları ve 1000 TL üzerindeki "aşırı" anomalileri işleme alma (Logla veya geç).<br><br>2. Normalizasyon: Departman isimlerini toupper() ile eşitle ki "math" ve "Math" aynı satırda toplansın.<br><br>3. Çok Boyutlu Dizi: harcama[dep, gun] += $3 yapısını kullan.<br><br>4. Matematiksel Kontrol: Satır ve Sütun toplamlarını eksiksiz hesapla.<br><br>5. Bonus (Wrap Denemesi): Eğer departman ismi 5 karakterden uzunsa, tabloda sadece ilk 5 karakterini ve yanına bir nokta koyarak bas (Örn: Scien.). |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN { 
    FS = ","
    # Günlerin sırasını manuel belirleyelim ki karışık basmasın
    sirali_gunler = "PAZARTESI,SALI,CARSAMBA,PERSEMBE,CUMA"
    split(sirali_gunler, gun_listesi, ",")
}

{
    # 1. Veri Temizliği (Header'ı atla ve anomalileri ele)
    if (NR == 1 || $3 < 0 || $3 > 1000) next;

    dep = toupper($1)
    gun = toupper($2)
    
    # 2. Çok Boyutlu Diziye Ekleme
    # AWK arkada bunu "MATH\034PAZARTESI" gibi bir anahtar yapar
    matris[dep, gun] += $3
    
    # Departmanları kayıt altında tut
    dep_listesi[dep] = 1
}

END {
    # --- BAŞLIKLARI BAS (Günler) ---
    printf "%-10s", "DEP/GUN"
    for (i=1; i<=5; i++) printf " | %-10s", gun_listesi[i]
    printf " | %-10s\n", "TOPLAM"
    print "-------------------------------------------------------------------------------"

    # --- SATIRLARI BAS (Departmanlar) ---
    for (d in dep_listesi) {
        # Wrap/Truncate Denemesi: 5 karakterden uzunsa kes
        dep_gorunum = (length(d) > 5) ? substr(d, 1, 5) "." : d
        printf "%-10s", dep_gorunum
        
        satir_toplam = 0
        for (i=1; i<=5; i++) {
            g = gun_listesi[i]
            deger = matris[d, g] # Eğer o gün harcama yoksa AWK 0 kabul eder
            printf " | %-10.2f", deger
            satir_toplam += deger
            sutun_toplam[g] += deger # Sütun toplamı için biriktir
        }
        printf " | %-10.2f\n", satir_toplam
        genel_toplam += satir_toplam
    }

    # --- ALT TOPLAMLARI BAS (Genel) ---
    print "-------------------------------------------------------------------------------"
    printf "%-10s", "GENEL"
    for (i=1; i<=5; i++) {
        g = gun_listesi[i]
        printf " | %-10.2f", sutun_toplam[g]
    
 | %-10.2f\n", genel_toplam
}
```
