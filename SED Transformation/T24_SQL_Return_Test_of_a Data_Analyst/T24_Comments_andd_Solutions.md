# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 77.5/10 | ***### Zorluk duzeyi:*** 7.5/10|
| SCENARIO:  | SENARYO: Freelance veri analisti olarak bir e-ticaret sitesinin ham satış verilerini (g24_sales.log) aldınız. Veriler çok karmaşık ve "kirli". Müşteri isimleri, satın alınan ürün kodları ve fiyatlar birbirine girmiş durumda. Sizden bu veriyi temizleyip bir "SQL Insert" sorgusu taslağına dönüştürmeniz isteniyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. History Transformation (YYYY-MM-DD): DD/MM/YYYY by capturing the dates in the format and changing their locations YYYY-MM-DD make it.
HINT: Input: 12/03/2026 -> Output: 2026-03-12 <br><br> 2. Price and Currency Manipulation: At the end of the line TL delete the phrase, at the beginning of the number $ put it and put it at the end .00 add it to "float" (decimal) format. <br>HINT: Input: 150TL -> Output: $150.00 <br><br> 3. Product Code Simplification: In parentheses (PROD-XYZ) just their structure SKU_XYZ make it. <br><br> 4. SQL Wrapping (Sarma): Shu shekilde palace the line of Her:<br> HINT: INSERT INTO sales VALUES ('Musteri_Adi', 'SKU_Kod', 'Tarih', 'Fiyat'); <br><br> 5. Automation (sed Script): All these complicated rules g24_transform.sed Write to a file named and sed -f g24_transform.sed g24_sales.log run it with the command. | 1. Fiyat Etiketleme: Dosyadaki tüm fiyat ibarelerinin (Örn: 150TL veya 200tl) başına PRICE: etiketi ekleyin ve TL kısımlarını silerek sonuna _USD yazın. (Örn: 150TL -> PRICE:150_USD). <br><br> 2. Ürün Kodu Temizliği: Ürün kodları parantez içinde geliyor: (PROD-123). Bu parantezleri kaldırın ve sadece SKU_123 formatına getirin. <br><br> 3. Tarih Formatı: DD/MM/YYYY formatında gelen tarihleri, veritabanı standardı olan YYYY-MM-DD formatına çevirin. (İpucu: 3 farklı grup (..)/(..)/(....) yakalayıp yerlerini \3-\2-\1 şeklinde değiştirin). <br><br> 4. SQL Taslağı: Her satırın başına INSERT INTO sales VALUES ( ve her satırın sonuna ); ekleyin. <br><br> 5. Zincirleme: Tüm bu işlemleri tek bir sed komut dosyasında (-f opsiyonu ile kullanmak üzere) bir dosyaya yazın ve uygulayın. |
| Golden Information: | Altin Bilgi:|
| sedWhen grouping in -E Using (Extended Regex), escape character before parentheses \ it eliminates the need to use it. This in turn increases readability by 100% in complex exchanges (such as the date format). | sed'de gruplandırma yaparken -E (Extended Regex) kullanmak, parantezlerden önce kaçış karakteri \ kullanma zorunluluğunu ortadan kaldırır. Bu da karmaşık değişimlerde (tarih formatı gibi) okunabilirliği %100 artırır. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E -e 's/([0-9]{1,2})\/([0-9]{1,2})\/([0-9]{4})/\3-\2-\1/g' \
-e 's/([0-9]+)TL/$\1.00/g' \
-e 's/\(([A-Z]+)-([0-9]+)\)/SKU_\2/g' \
-e 's/([a-z]+)_([a-z]+) \| (SKU_[0-9]+) \| ([0-9-]+) \| (\$[0-9.]+)/INSERT INTO sales VALUES ('\''\1'\'', '\''\2'\'', '\''\3'\'', '\''\4'\'', '\''\5'\'');/' g24_sales.log
```
