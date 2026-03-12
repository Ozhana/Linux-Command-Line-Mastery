# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 5.5/5 | ***### Zorluk duzeyi:*** 5.5/10|
| SCENARIO: The system logs you have (g22_security_audit.log) contains a lot of "noise" (noise). Unnecessary "INFO" messages, empty lines, and records outside a certain date range make your analysis difficult. As a cybersecurity expert, you need to prune the file to focus only on “critical” and “suspicious” data. | SENARYO: Elinizdeki sistem logları (g22_security_audit.log) çok fazla "gürültü" (noise) içeriyor. Gereksiz "INFO" mesajları, boş satırlar ve belirli bir tarih aralığı dışındaki kayıtlar analizinizi zorlaştırıyor. Bir siber güvenlik uzmanı olarak, sadece "kritik" ve "şüpheli" veriye odaklanmak için dosyayı budamanız gerekiyor |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Eliminating Unnecessary: All in the file INFO completely delete the log lines at the level. <br> (Hint: d command). <br><br> 2. Empty Satir Promotion: Wipe the lumbar tum empty rows of calan thum after working on the veya urea üretiminde. (Power: ^$ cull the regex Japanese). <br><br>  3. Range Oriented Erase: The first 5 lines (headings) and the last 5 lines (closing notes) of the log file should be excluded from analysis. Delete these lines. <br><br> 4. IP Masking (Advanced): Inside FAILED_ACCESS star the last digit of the IP addresses in the last rows (Ex: 192.168.1.1 -> 192.168.1.*). <br><br> 5. Summary Report: Only FAILED_ACCESS or CRITICAL press the containing lines into the terminal but do not change anything in the original file. (Hint: -n and the p combination). | 1. Gereksizleri Eleme: Dosyadaki tüm INFO seviyesindeki log satırlarını tamamen silin. (İpucu: d komutu). <br><br> 2. Boş Satır Temizliği: Dosya üretiminde oluşan veya işlem sonrası kalan tüm boş satırları tek hamlede silin. (İpucu: ^$ regex yapısını kullanın). <br><br> 3. Aralık Odaklı Silme: Log dosyasının ilk 5 satırı (başlıklar) ve son 5 satırı (kapanış notları) analiz dışı kalmalı. Bu satırları silin. <br><br> 4. IP Maskeleme (Gelişmiş): İçinde FAILED_ACCESS geçen satırlardaki IP adreslerinin son hanesini yıldızlayın (Örn: 192.168.1.1 -> 192.168.1.*). <br><br> 5. Özet Rapor: Sadece FAILED_ACCESS veya CRITICAL içeren satırları terminale basın ama orijinal dosyada hiçbir şeyi değiştirmeyin. (İpucu: -n ve p kombinasyonu). |
| Golden Knowledge : | Altin Bilgi : |
| sed in the d (delete) command, s It works with a similar addressing logic as the (Substitute) command. For example sed '1,5d' dosya if you say so, he throws the first 5 lines and prints the rest. sed '/pattern/d' it completely destroys the row containing that pattern. | sed'de d (delete) komutu, s (substitute) komutuyla benzer bir adresleme mantığıyla çalışır. Örneğin sed '1,5d' dosya derseniz ilk 5 satırı atar, geri kalanını basar. sed '/pattern/d' ise o deseni içeren satırı komple yok eder. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. sed '/info/Id' g22_security_audit.log > g22_A_security_audit.log ; grep -i "info" g22_A_security_audit.log
2. sed -i '/^$/d' g22_A_security_audit.log 
3. sed -i '1,5d' g22_A_security_audit.log ; head -n -5 g22_A_security_audit.log > temp_g22_A_security_audit.log ; cat temp_g22_A_security_audit.log >g22_A_security_audit.log 
4. sed -Ei 's/(SOURCE_IP:[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)[0-9]{1,3}/\1*/g' g22_A_security_audit.log
5. sed -n '/FAILED_ACCESS\|CRITICAL/p' g22_A_security_audit.log
```
