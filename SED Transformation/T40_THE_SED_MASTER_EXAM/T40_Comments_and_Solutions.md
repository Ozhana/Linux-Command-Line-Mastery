# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: In your hands a very complex and “dirty” log file (final_exam.log) there is. This file contains both user data and junk system garbage. | SENARYO: Elinizde çok karmaşık ve "kirli" bir log dosyası (final_exam.log) var. Bu dosya hem kullanıcı verilerini hem de gereksiz sistem çöplerini içeriyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Format Conversion: USER: [name] \| IP: [ip] \| ROLE: [role] find the lines and [ROLE] -> [NAME] (IP: [IP]) convert to format. Role names completely UPPERCASE LETTER do (\U).<br><br>2. Numerical Filtering: If IP address 192. if it starts with, consider this user "Local" and move to the end of the line [LOCAL_ACCESS] add.<br><br>3. Multiple Line Cleaning: If in a line ERROR it says and in the next line CODE: 404 if it does, combine these two into a single line and start it [CRITICAL_ERR] sheep. <br><br>4. Injection: To the very beginning of the file --- START OF AUDIT: [TARİH] --- and to the very end --- END OF REPORT --- add. <br><br>5. Bonus: Inside TRASH or DEBUG completely destroy all worded lines from the report. | 1. Format Dönüşümü: USER: [name] \| IP: [ip] \| ROLE: [role] satırlarını bulun ve [ROLE] -> [NAME] (IP: [IP]) formatına çevirin. Rol isimlerini tamamen BÜYÜK HARF yapın (\U). <br><br>2. Sayısal Filtreleme: Eğer IP adresi 192. ile başlıyorsa, bu kullanıcıyı "Local" kabul edin ve satırın sonuna [LOCAL_ACCESS] ekleyin.<br><br>3. Çoklu Satır Temizliği: Eğer bir satırda ERROR yazıyor ve bir sonraki satırda CODE: 404 geliyorsa, bu ikiliyi tek bir satırda birleştirin ve başına [CRITICAL_ERR] koyun. <br><br>4. Enjeksiyon: Dosyanın en başına --- START OF AUDIT: [TARİH] --- ve en sonuna --- END OF REPORT --- ekleyin.<br><br>5. Bonus: İçinde TRASH veya DEBUG kelimesi geçen tüm satırları rapordan tamamen imha edin. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee "1i --- START OF AUDIT: $(date +%F\ %T) ---" \
    -e 's/^USER: (.*) \| IP: (.*) \| ROLE: (.*)/\U\3 -> \1 (IP: \2)/' \
    -e '/192\./s/$/ [LOCAL_ACCESS]/' \
    -e '/ERROR/{N; /CODE: 404/s/^/[CRITICAL_ERR] /; s/\n/ /}' \
    -e '/Trash/Id; /DEBUG/Id' \
    -e '$a --- END OF REPORT --- ()' \
    g40_final_exam.log | sed "/--- ()/s/--- ()/--- $(date)/"

```
