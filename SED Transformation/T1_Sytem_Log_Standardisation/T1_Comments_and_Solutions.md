# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: Access logs for the server in your school (g21_system_logs.txt), was hired by different staff at different times. Hence the inconsistencies in the formats. You also need to mask some critical system information and update old version tags before presenting these logs to the school administration. | SENARYO: Okulunuzdaki sunucuya ait erişim logları (g21_system_logs.txt), farklı zamanlarda farklı personeller tarafından tutulmuş. Bu nedenle formatlarda tutarsızlıklar var. Ayrıca bu logları okul yönetimine sunmadan önce bazı kritik sistem bilgilerini maskelemeniz ve eski versiyon etiketlerini güncellemeniz gerekiyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Standardization: All in the file old_v1 your phrases stable_v2.0 change to. (Simulate the change in the terminal first). <br><br> 2. Security Masking (Admin): root in the lines where the user passes, the username PROTECTED_ADMIN change to. <br><br> 3. Localhost Cleaning: All 127.0.0.1 (localhost) IP addresses for general readability of the report internal_loopback replace text with. <br><br> 4. Verification (Grep Integration): To confirm that your IP change was successful sed print out grep "internal_loopback" pipe to command (\|) check by doing. <br><br> 5. Permanent Registration: All these operations with a single chain of command (or -e using) the file itself (-iApply ) and print the first 10 lines. | 1. Standardizasyon: Dosyadaki tüm old_v1 ibarelerini stable_v2.0 olarak değiştirin. (Değişikliği önce terminalde simüle edin). <br><br> 2. Güvenlik Maskeleme (Admin): root kullanıcısının geçtiği satırlarda, kullanıcı adını PROTECTED_ADMIN olarak değiştirin. <br><br> 3. Localhost Temizliği: Tüm 127.0.0.1 (localhost) IP adreslerini, raporun genel okunabilirliği için internal_loopback metni ile değiştirin. <br><br> 4. Doğrulama (Grep Entegrasyonu): Yaptığınız IP değişikliğinin başarılı olduğunu teyit etmek için sed çıktısını grep "internal_loopback" komutuna pipe (\|) yaparak kontrol edin. <br><br> 5. Kalıcı Kayıt: Tüm bu işlemleri tek bir komut zinciriyle (veya -e kullanarak) dosyanın kendisine (-i) uygulayın ve ilk 10 satırı yazdırın. |
| HINTS | IPUCLARI |
| A. sed -e 's/A/B/g' -e 's/C/D/g' dosyaits structure makes multiple changes at once. <br> B. s/aranan/yeni/g at the end g (global) changes all matches in the row. If two in a row 127.0.0.1 if g if you don't use it, only the first one changes. | A. sed -e 's/A/B/g' -e 's/C/D/g' dosya yapısı birden fazla değişikliği tek seferde yapar. <br> s/aranan/yeni/g sonundaki g (global), satırdaki tüm eşleşmeleri değiştirir. Eğer bir satırda iki tane 127.0.0.1 varsa g kullanmazsanız sadece ilki değişir |
| sed the biggest fear when working with is corrupting the original data. -i be sure to see the output on the screen before using the (Inplace) option. If you want to be safe -i.bak you can use; this command creates a backup of the original file and makes the change to the original file. | sed ile çalışırken en büyük korku orijinal veriyi bozmaktır. -i (inplace) opsiyonunu kullanmadan önce mutlaka çıktıyı ekranda görün. Eğer kendinizi sağlama almak isterseniz -i.bak kullanabilirsiniz; bu komut orijinal dosyanın bir yedeğini oluşturur ve değişikliği asıl dosyada yapar. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. sed 's/old_v1/stable_v2.0/g' g21_system_logs.txt > g21_A_system_logs.txt ; grep -E "old|stable" g21_A_system_logs.txt 

2. sed -i 's/root/PROTECTED_ADMIN/Ig' g21_A_system_logs.txt ; grep -E "root|PROTECTED_ADMIN" g21_A_system_logs.txt 

3. ve 4. sed -i 's/127.0.0.1/internal_loopback/g' g21_A_system_logs.txt ; grep -E "127|internal_loopback" g21_A_system_logs.txt

5. sed -i '1,10s/127.0.0.1/internal_loopback/g' g21_A_system_logs.txt ; grep -E "127|internal_loopback" g21_A_system_logs.txt
```
