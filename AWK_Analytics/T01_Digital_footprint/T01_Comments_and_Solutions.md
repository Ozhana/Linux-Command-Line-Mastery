# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 6/10 | ***### Zorluk duzeyi:*** 6/10|
| SCENARIO: we're starting with the first mission. In this task, the basic pillar logic of AWK and BEGIN/END we will use blocks. <br><br>You are a data analyst for a freelance platform. He has a complex log file containing the movements of users on the platform. This file contains the user ID, transaction type, earnings, transaction time and device information from which he logged into the platform. | SENARYO: Bu görevde AWK'ın temel sütun mantığını ve BEGIN/END bloklarını kullanacağız. <br><br>Bir freelance platformunun veri analistisin. Elinde platformdaki kullanıcıların hareketlerini içeren karmaşık bir log dosyası var. Bu dosyada kullanıcı ID'si, işlem tipi, kazanç, işlem süresi ve platforma giriş yaptığı cihaz bilgisi yer alıyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only PROJECT_COMPLETE find the rows and print the amount earned by the user ID on the screen.<br><br>2. Processing time (duration) Find the number of transactions over 60 minutes (Which variable can you count by increasing?). <br><br>3. Total over the entire file amount calculate the (earnings) value and at the end END print on block. <br><br>4. Device information (last column) only the first 3 characters of the rows with “Fedora_v43” (substr using) and print the line number. <br><br>5. Reporting: "FREELANCE FINANCIAL REPORT" heading at the beginning of the output and "TOTAL TRANSACTION: [NR]" information at the end printf add aligned using. | 1. Sadece PROJECT_COMPLETE olan satırları bul ve kullanıcı ID'si ile kazandığı miktarı ekrana yazdır.<br><br>2. İşlem süresi (duration) 60 dakikadan fazla olan işlemlerin sayısını bul (Hangi değişkeni artırarak sayabilirsin?).<br><br>3. Tüm dosya boyunca toplam amount (kazanç) değerini hesapla ve en sonda END bloğunda yazdır.<br><br>4. Cihaz bilgisi (son sütun) "Fedora_v43" olan satırların sadece ilk 3 karakterini (substr kullanarak) ve satır numarasını yazdır. <br><br>5. Raporlama: Çıktının en başına "FREELANCE FINANSAL RAPOR" başlığını, en sonuna da "TOPLAM ISLEM: [NR]" bilgisini printf kullanarak hizalı şekilde ekle. |
| Golden Information: | Altin Bilgi: |
| 1. $1, $2, ... $NF: Field variables. $NF always last one gives column.<br><br>2. NR: (Number of Records) The number of the currently processed line.<br><br>3. NF: (Number of Fields) The total number of columns in that row.<br><br>4. printf: To print data in aligned and professional format (as in C language). | 1. $1, $2, ... $NF: Alan değişkenleri. $NF her zaman sonuncu sütunu verir.<br><br>2. NR: (Number of Records) O an işlenen satırın numarası.<br><br>3. NF: (Number of Fields) O satırdaki toplam sütun sayısı.<br><br>4. printf: Veriyi hizalı ve profesyonel formatta yazdırmak için (C dilindeki gibi). |
| Analytical Question: | Analitik Soru: |
|  | Eğer dosyadaki sütun ayırıcı boşluk değil de virgül (CSV) olsaydı, AWK'a bunu nasıl söylerdin? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  | Soru: Virgül (CSV) olsaydı ne yapardık? <br><br>Cevap: İki yolun var. Ya komutu çalıştırırken -F"," parametresini eklersin ya da BEGIN bloğu içine FS="," (Field Separator) yazarsın. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN { 
    # 5. Madde: Başlık
    printf "%-10s | %-15s | %-10s | %-10s\n", "USER_ID", "ACTION", "AMOUNT", "DEVICE"
    print "------------------------------------------------------------"
    toplam = 0
    uzun_islem = 0
}

{
    # 1. Madde: Sadece PROJECT_COMPLETE olanlar
    if ($2 == "PROJECT_COMPLETE") {
        
        # 4. Madde: Cihaz Fedora_v43 ise ilk 3 karakteri al (substr)
        cihaz = $5
        if (cihaz == "Fedora_v43") {
            cihaz = substr(cihaz, 1, 3)
        }

        # Çıktıyı hizalı yazdıralım
        printf "%-10s | %-15s | %-10.2f | %-10s\n", $1, $2, $3, cihaz
        
        # 3. Madde: Toplam kazancı hesapla
        toplam += $3
    }

    # 2. Madde: 60 dakikadan fazla sürenleri say (4. sütun "90min" formatında olduğu için int() ile temizle)
    if (int($4) > 60) {
        uzun_islem++
    }
}

END {
    print "------------------------------------------------------------"
    print "FREELANCE FINANSAL RAPORU"
    printf "Toplam Kazanç: %.2f USD\n", toplam
    print "60 Dakikayı Geçen İşlem Sayısı: " uzun_islem
    print "TOPLAM ISLEM (Satır Sayısı): " NR
}
```
