# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: You have daily sales data of a market (g27_sales_raw.csv). However, the data is in a structure called "Long Format", where each process is written one under the other. Before putting this data from you into an analysis tool sed just clean it with Product Name and Total Sales (Pieces x Price) you are asked to simplify it as follows. | SENARYO: Elinizde bir marketin günlük satış verileri var (g27_sales_raw.csv). Ancak veriler "Long Format" denilen, her işlemin alt alta yazıldığı bir yapıda. Sizden bu veriyi, bir analiz aracına sokmadan önce sed ile temizleyip, sadece Ürün İsmi ve Toplam Satış (Adet x Fiyat) şeklinde basitleştirmeniz isteniyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Arithmetic Preparation: In every line ADET:5 \| FIYAT:10 there is a structure like this. sed he can't do math, but you put the data into a format like this: URUN_ADI -> (5*10). <br><br> 2. Fly Unnecessary Columns: Completely delete columns such as sales representative name and branch code. <br><br> 3. Category Labeling: If the product name is in it PRO_ If (Professional Series) is mentioned, at the beginning of the line [PREMIUM] add tag. <br><br> 4. Sequential Cleaning: The first 2 lines (headings) and the last line (subsum of totals) in the file should be excluded from analysis. <br><br> 5. Advanced Filtering: Only PREMIUM what is and the price 50 leave products with more than units on the screen and delete the others. | 1. Aritmetik Hazırlık: Her satırda ADET:5 \| FIYAT:10 gibi bir yapı var. sed matematik yapamaz ama siz veriyi şöyle bir formata sokun: URUN_ADI -> (5*10). <br><br> 2. Gereksiz Kolonları Uçur: Satış temsilcisi adı ve şube kodu gibi kolonları tamamen silin. <br><br> 3. Kategori Etiketleme: Eğer ürün ismi içinde PRO_ (Profesyonel Seri) geçiyorsa, satırın başına [PREMIUM] etiketi ekleyin. <br><br> 4. Sıralı Temizlik: Dosyadaki ilk 2 satır (başlıklar) ve son satır (toplamlar alt toplamı) analiz dışı bırakılmalı. <br><br> 5. Gelişmiş Filtreleme: Sadece PREMIUM olan ve fiyatı 50 birimden fazla olan ürünleri ekranda bırakın, diğerlerini sili |
| Golden Information: (/pattern/ { commands }) | Altın Bilgi: (/pattern/ { commands }): |
| sed -n using (silent mode) /pattern/ { p } proceeding with logic, complex filtering d it’s much safer than bothering with the (delete) command. Because you just "tweeze" the data you want. | Bir satırda belirli bir kelime geçiyorsa birden fazla sed komutunu sadece o satıra uygulamak için süslü parantez kullanabilirsiniz:
sed -n '/PRO_/ { s/ITEM://; s/QTY/ADET/; p }' dosya
Bu, sed'i adeta bir mini programlama dili gibi kullanmanızı sağlar. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E -e '/INFO/Id' -e '/^$/d' g22_security_audit.log | tail -n +6 | head -n -5

OR

n=$(sed -E -e '/INFO/Id' -e '/^$/d' g22_security_audit.log | wc -l)
start=6
end=$((n - 5))

sed -E -e '/INFO/Id' -e '/^$/d' g22_security_audit.log | sed -n "${start},${end}p"

OR -- FULL ANSWER IN ONE LINE --

sed -Ee 's/ITEM:([^[:space:]]*) \| QTY:([0-9]{1,3}) \| PRICE:([0-9]{1,4})/& \| \1 -> \2*\3/g; s/ID:[0-9]{1,5} \| BRANCH:[^\|]+ \| //g; /PRO/s/^/[PREMIUM] /g; /[PREMIUM]/!d; /PRICE:5[0-9]{1,4}/!d' g27_sales_raw.csv | head -n -2 | tail -n +2
```
