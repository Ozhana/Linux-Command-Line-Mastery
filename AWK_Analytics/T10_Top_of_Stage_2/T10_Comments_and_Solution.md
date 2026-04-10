# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: List of users on the Fedora server (/etc/passwd we will compare the list of those who logged into the system that day with similar).<br><br>File 1 (users.txt): username:full_name:department (Ex: ozhan:Dr_Ozhan:Math)<br><br>File 2 (logins.txt): username:login_count:last_ip (Ex: ozhan:5:192.168.1.50) | SENARYO: Fedora sunucundaki kullanıcı listesi (/etc/passwd benzeri) ile o gün sisteme login olanların listesini karşılaştıracağız.<br><br>Dosya 1 (users.txt): username:full_name:department (Örn: ozhan:Dr_Ozhan:Math)<br><br>Dosya 2 (logins.txt): username:login_count:last_ip (Örn: ozhan:5:192.168.1.50) |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Different Separator: Not a comma this time, colon (:) use it.<br><br>2. Join: Users username match via.<br><br>3. Multiple Filtering:<br><br>- If a user is in the list but has never logged in: "PASSIVE USER"<br><br>- But if you are logged in department value IT if not and login_count If more than 10: "SUSPICIOUS INTENSITY"<br><br>- If everything is normal: "SAFE"<br><br>4. Dynamic Report: Department from the terminal -v dep="Math" when you send it as follows, it should only give a special report to that department. | Farklı Ayırıcı: Bu sefer virgül değil, iki nokta üst üste (:) kullan.<br><br>Join: Kullanıcıları username üzerinden eşleştir.<br><br>Çoklu Filtreleme:<br><br>Eğer bir kullanıcı listede var ama hiç login olmamışsa: "PASİF KULLANICI"<br><br>Eğer login olmuş ama department değeri IT değilse ve login_count 10'dan fazlaysa: "ŞÜPHELİ YOĞUNLUK"<br><br>Eğer her şey normalse: "GÜVENLİ"<br><br>Dinamik Rapor: Departmanı terminalden -v dep="Math" şeklinde gönderdiğinde sadece o departmana özel rapor versin. |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN { 
    FS=":";
    printf "%-10s | %-12s | %-15s | %-20s |\n", "Full Name", "Login Count", "Last IP", "Status";
    print "-------------------------------------------------------------------------";
}

NR == FNR {
    # Birinci dosya: users.txt
    # Sadece istenen departmandaysa veya departman belirtilmemişse hafızaya al
    if (dep == "" || $3 == dep) {
        full_name[$1] = $2;
        department[$1] = $3;
    }
    next;
}

{
    # İkinci dosya: logins.txt
    if ($1 in full_name) {
        # Mantık: IT değilse VE login > 10 ise ŞÜPHELİ
        if (department[$1] != "IT" && $2 > 10) {
            durum = "ŞÜPHELİ YOĞUNLUK";
        } else {
            durum = "GÜVENLİ";
        }
        
        printf "%-10s | %-12d | %-15s | %-20s |\n", full_name[$1], $2, $3, durum;
        delete full_name[$1]; # İşlendi, sil.
    }
}

END {
    # Geriye kalanlar login olmayan (Pasif) kullanıcılardır
    for (usr in full_name) {
        printf "%-10s | %-12s | %-15s | %-20s |\n", full_name[usr], "0", "N/A", "PASIF KULLANICI";
    }
    print "-------------------------------------------------------------------------";
}
```
