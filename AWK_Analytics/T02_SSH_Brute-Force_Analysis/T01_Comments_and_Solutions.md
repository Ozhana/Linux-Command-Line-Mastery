# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 6.5/10 | ***### Zorluk duzeyi:*** 6.5/10|
| SCENARIO:  | SENARYO: Sunucuna ait /var/log/auth.log dosyasının bir simülasyonu üzerinde çalışacaksın. Bir saldırgan, farklı kullanıcı adları ve IP adresleri üzerinden sisteme sızmaya çalışıyor. Senin görevin, bu log yığınını analiz edip "şüpheli" hareketleri raporlamak. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Kritik Hata Filtresi: Durumu (status) Failed VEYA Invalid user olan tüm satırları bul ve sadece zaman, kullanıcı adı ve IP adresini yazdır.<br><br>2. Root Alarmı: Eğer kullanıcı adı root ise ve durum Failed ise satırın başına "[DIKKAT]" ibaresi ekle.<br><br>3. IP Sınıflandırma: IP adresi 192.168. ile başlıyorsa (Yerel Ağ), bu satırları terminale yazdırma (Sadece dış saldırılara odaklanmak istiyoruz). !~ operatörünü kullanmayı dene.<br><br>4. İstatistik Paneli: Kaç tane Accepted (başarılı giriş) ve kaç tane Failed (başarısız) işlem olduğunu sayıp END bloğunda bir tablo olarak göster.<br><br>5. Gelişmiş Filtre: Port numarası (son sütun) 50.000'den büyük olan ve durumu Failed olan satırları bul. |
| Golden Information: | Altin Bilgi: |
|  | 1. Karşılaştırma Operatörleri: == (eşit), != (eşit değil), ~ (içeriyor/regex eşleşmesi), !~ (içermiyor). <br><br>2. Mantıksal Operatörler: && (VE), || (VEYA). <br><br>3. Hizalama (printf): Veriyi sütun sütun tertemiz dizmek. <br><br>4. AWK'da ~ işareti "Regular Expression (Regex)" kullanmanı sağlar. Eğer /pattern/ içine bir şey yazarsan AWK o satırda o deseni arar.|
| Analytical Question: | Analitik Soru: |
|  | AWK içinde bir kelimenin sadece bir kısmını (örneğin IP'nin ilk 3 hanesini) kontrol etmek için if ($9 ~ /^192/) gibi bir ifade kullanabilir miyiz? Bu işaret (^) ne anlama gelir? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN {
    # Başlıkları ve sayaçları hazırla
    printf "%-20s | %-12s | %-10s | %-15s\n", "ZAMAN", "DURUM", "USER", "IP"
    print "----------------------------------------------------------------------"
    accepted = 0; failed = 0;
}

{
    zaman = $1 " " $2 " " $3
    
    # 3. Madde: Yerel ağdan gelenleri (192.168.x.x) direkt atla (next komutu sonraki satıra geçer)
    if ($0 ~ /from 192\.168\./) { next }

    # Sayacımız için genel istatistik
    if ($6 == "Accepted") { accepted++ }
    if ($6 == "Failed" || $6 == "Invalid") { failed++ }

    # 1. & 2. Madde: Kritik Hata ve Root Alarmı
    if ($6 == "Failed" || $6 == "Invalid") {
        
        # Sütunları dinamik bulma: "from" kelimesinden önceki kullanıcıdır, sonraki IP'dir
        # Ama şimdilik senin saydığın sabit sütunlar üzerinden gidelim:
        user = ($6 == "Invalid") ? $11 : $9
        ip = ($6 == "Invalid") ? $13 : $11
        status = ($6 == "Invalid") ? "Invalid User" : "Failed Pwd"

        # Root kontrolü
        alarm = (user == "root") ? "[DIKKAT] " : ""

        # 5. Madde: Port kontrolü (Son sütun $NF)
        if (int($NF) > 50000) {
            printf "%s%-20s | %-12s | %-10s | %-15s (Port: %s)\n", alarm, zaman, status, user, ip, $NF
        }
    }
}

END {
    print "----------------------------------------------------------------------"
    print "SİBER GÜVENLİK ÖZET RAPORU"
    printf "Başarılı Giriş: %d | Başarısız Deneme: %d\n", accepted, failed
    print "Toplam İncelenen Kayıt: " NR
}
```
