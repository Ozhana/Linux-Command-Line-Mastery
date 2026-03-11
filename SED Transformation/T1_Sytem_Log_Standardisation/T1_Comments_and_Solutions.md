# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: Access logs for the server in your school (g21_system_logs.txt), was hired by different staff at different times. Hence the inconsistencies in the formats. You also need to mask some critical system information and update old version tags before presenting these logs to the school administration. | SENARYO: Okulunuzdaki sunucuya ait erişim logları (g21_system_logs.txt), farklı zamanlarda farklı personeller tarafından tutulmuş. Bu nedenle formatlarda tutarsızlıklar var. Ayrıca bu logları okul yönetimine sunmadan önce bazı kritik sistem bilgilerini maskelemeniz ve eski versiyon etiketlerini güncellemeniz gerekiyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Standardization: All in the file old_v1 your phrases stable_v2.0 change to. (Simulate the change in the terminal first). <br><br> 2. Security Masking (Admin): root in the lines where the user passes, the username PROTECTED_ADMIN change to. <br><br> 3. Localhost Cleaning: All 127.0.0.1 (localhost) IP addresses for general readability of the report internal_loopback replace text with. <br><br> 4. Verification (Grep Integration): To confirm that your IP change was successful sed print out grep "internal_loopback" pipe to command (|) check by doing. <br><br> 5. Permanent Registration: All these operations with a single chain of command (or -e using) the file itself (-iApply ) and print the first 10 lines. | 1. Gereksizleri Eleme: Dosyadaki tüm INFO seviyesindeki log satırlarını tamamen silin. (İpucu: d komutu).v<br><br> 2. Boş Satır Temizliği: Dosya üretiminde oluşan veya işlem sonrası kalan tüm boş satırları tek hamlede silin. (İpucu: ^$ regex yapısını kullanın). <br><br> 3. Aralık Odaklı Silme: Log dosyasının ilk 5 satırı (başlıklar) ve son 5 satırı (kapanış notları) analiz dışı kalmalı. Bu satırları silin. <br><br> 4. IP Maskeleme (Gelişmiş): İçinde FAILED_ACCESS geçen satırlardaki IP adreslerinin son hanesini yıldızlayın (Örn: 192.168.1.1 -> 192.168.1.*). <br><br> 5. Özet Rapor: Sadece FAILED_ACCESS veya CRITICAL içeren satırları terminale basın ama orijinal dosyada hiçbir şeyi değiştirmeyin. (İpucu: -n ve p kombinasyonu). |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. sed 's/old_v1/stable_v2.0/g' g21_system_logs.txt > g21_A_system_logs.txt ; grep -E "old|stable" g21_A_system_logs.txt 

2. sed -i 's/root/PROTECTED_ADMIN/Ig' g21_A_system_logs.txt ; grep -E "root|PROTECTED_ADMIN" g21_A_system_logs.txt 

3. ve 4. sed -i 's/127.0.0.1/internal_loopback/g' g21_A_system_logs.txt ; grep -E "127|internal_loopback" g21_A_system_logs.txt

5. sed -i '1,10s/127.0.0.1/internal_loopback/g' g21_A_system_logs.txt ; grep -E "127|internal_loopback" g21_A_system_logs.txt
```
