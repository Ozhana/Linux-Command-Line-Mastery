# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 9.5/10 | ***### Zorluk duzeyi:*** 9.5/10|
| SCENARIO: As a system administrator you have a "scrambled" (shuffled) log file (g31_obfuscated.log). In this file, keywords and their values are on different lines, and sometimes even "garbage data" is inserted. Your job is to disperse these scattered pieces sedMerge using 's drawer (Hold Space) and produce a clean report. | SENARYO: Bir sistem yöneticisi olarak elinizde "karıştırılmış" (shuffled) bir log dosyası var (g31_obfuscated.log). Bu dosyada anahtar kelimeler ve onlara ait değerler farklı satırlarda, hatta bazen araya "çöp veriler" girmiş durumda. Sizin göreviniz, bu dağınık parçaları sed'in çekmecesini (Hold Space) kullanarak birleştirmek ve temiz bir rapor üretmek. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|1. Key Capture: If row KEY: [İSİM] if it starts with, copy this name to the drawer (Hold Space) (h).<br><br>2. Value Combination: If row VALUE: [VERİ] if it starts with, take the name in the drawer and add it next to this data (G).<br><br>3. Garbage Cleaning: Inside IGNORE or TRASH destroy all passing lines without any processing (d). <br><br>4. Formatting: Make the output: ENTRY -> İSİM \| DATA -> VERİ.<br><br>5.  Dynamic Change: If DATA in part CRITICAL if the word is mentioned, at the end of the line [!!!] put the sign. |1. Anahtar Yakalama: Eğer satır KEY: [İSİM] ile başlıyorsa, bu ismi çekmeceye (Hold Space) kopyalayın (h). <br><br>2. Değer Birleştirme: Eğer satır VALUE: [VERİ] ile başlıyorsa, çekmecedeki ismi alıp bu verinin yanına ekleyin (G). <br><br>3. Çöp Temizliği: İçinde IGNORE veya TRASH geçen tüm satırları hiçbir işleme sokmadan yok edin (d). <br><br>4. Formatlama: Çıktıyı şu hale getirin: ENTRY -> İSİM | DATA -> VERİ.<br><br>5. Dinamik Değişim: Eğer DATA kısmında CRITICAL kelimesi geçiyorsa, satırın en sonuna [!!!] işareti koyun. |
| Golden Information: | Altin Bilgi: |
| Small g: It takes what's in the drawer, what's on the desktop (pattern space) he writes on it. Old data is deleted. <br><br>Big G: He takes what's in the drawer, what's on the desktop adds below (as a new line).<br><br>You are on this mission G using two data one under the other, then s/\n/ / you will marry them. | Küçük g: Çekmecedekini alır, masaüstündekinin (pattern space) üstüne yazar. Eski veri silinir.<br><br>Büyük G: Çekmecedekini alır, masaüstündekinin altına ekler (yeni bir satır olarak). <br><br>Siz bu görevde G kullanarak iki veriyi alt alta getirip, sonra s/\n/ / ile onları evlendireceksiniz. |
| Analytical Question: | Analitik Soru: |
| Let's say one KEY the line came and you threw it in the drawer. But then one VALUE there was no line, 10 "garbage" lines entered. sedDoes 's drawer (Hold Space) protect data during this time? Or does the drawer reset every time you read a line? | Diyelim ki bir KEY satırı geldi ve çekmeceye attınız. Ama hemen ardından bir VALUE satırı gelmedi, araya 10 tane "çöp" satırı girdi. sed'in çekmecesi (Hold Space) bu süre zarfında veriyi korur mu? Yoksa her satır okuduğunda çekmece sıfırlanır mı? |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E '/KEY:/h; /VALUE:/{G; s/\n/  /}; /IGNORE/Id; /TRASH/Id; /^KEY:/d; s/VALUE:[[:space:]]([[:alpha:]_]+)[[:space:]]{2}KEY:[[:space:]]([[:alpha:]_]+)$/ENTRY -> \2 \| DATA -> \1 /g; /CRITICAL/s/$/  [!!!]/Ig' g31_obfuscated.log


sed -nE '/KEY:/h; /VALUE:/{G; s/\n/ /gp}' g31_obfuscated.log | sed -E 's/VALUE:[[:space:]]+([[:alpha:]_]+)[[:space:]]+KEY:[[:space:]]+([[:alpha:]_]+)[[:space:]]*$/ENTRY -> \2 \| DATA -> \1/g'
```
``` bash
ClassIn returnDescriptionExample Usage[:alpha:]A-Za-zJust letters.[[:alpha:]]+(Captures words)[:alnum:]A-Za-z0-9Letters and Numbers.[[:alnum:]]+(Captures IDs)[:digit:]0-9Just numbers.[[:digit:]]{3}(3 digit number)[:lower:]a-zJust lowercase letters.[[:lower:]]+[:upper:]A-ZCapital letters only.[[:upper:]]+[:space:]\t\n\v\f\rAll kinds of gaps.[[:space:]]+[:punct:].,!?;:-etc.Punctuation.[[:punct:]](Finding sentence end)[:blank:]spaceand the tabHorizontal spaces only.[[:blank:]]
```
