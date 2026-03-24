# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: sed it is not actually capable of adding or subtracting numbers (because it sees everything as text/string). But we sed'i character based we can turn it into a calculator. <br><br>You have an inventory list (g37_inventory.txt). Stocks of some products have fallen to critical levels. <br><br>Format: PROD_ID: [ID] \| STOCK: [QTY] \| REORDER: [YES/NO] | SENARYO: sed aslında sayıları toplama veya çıkarma yeteneğine sahip değildir (çünkü her şeyi metin/string olarak görür). Ancak biz sed'i karakter bazlı bir hesap makinesine dönüştürebiliriz. <br><br>Bir envanter listeniz var (g37_inventory.txt). Bazı ürünlerin stokları kritik seviyeye düşmüş. <br><br>Format: PROD_ID: [ID] \| STOCK: [QTY] \| REORDER: [YES/NO] |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Stock Control: If STOCK if its value is single digit (0-9), next to this product [CRITICAL] add the phrase. <br><br>2. Automatic Order: If stock CRITICAL ise, REORDER: NO part of it REORDER: YES change to. <br><br>3. Numerical Conversion (Hard Part): In stock 0 (zero) as text wherever you see it OUT_OF_STOCK write. <br><br>4. Bonus (Mental Nerve): Only sed using, STOCK: 9 what happened STOCK: 10 can you? (Tip: You can't do numerical addition, just s/9/10/ you should make a text replacement like this). | 1. Stok Kontrolü: Eğer STOCK değeri tek haneliyse (0-9), bu ürünün yanına [CRITICAL] ibaresini ekleyin. <br><br>2. Otomatik Sipariş: Eğer stok CRITICAL ise, REORDER: NO kısmını REORDER: YES olarak değiştirin. <br><br>3. Sayısal Dönüşüm (Zor Kısım): Stokta 0 (sıfır) gördüğünüz her yere metin olarak OUT_OF_STOCK yazın. <br><br>4. Bonus (Zihni Sinir): Sadece sed kullanarak, STOCK: 9 olanları STOCK: 10 yapabilir misiniz? (İpucu: Sayısal toplama yapamazsınız, sadece s/9/10/ gibi bir metin değişimi yapmalısınız). |
| Golden Information: | Altin Bilgi: |
| STOCK: 9'u 10 be careful when doing it; if STOCK: 19 if there is, that too 110 you can! That's why it's in regex word boundaries ([[:space:]] or \| you should use the sign) as an anchor. | STOCK: 9'u 10 yaparken dikkatli olun; eğer STOCK: 19 varsa onu da 110 yapabilirsiniz! Bu yüzden regex'te kelime sınırlarını ([[:space:]] veya \| işaretini) çapa olarak kullanmalısınız. |
| Analytical Question: | Analitik Soru: |
| Performing a numerical magnitude comparison in a text-based tool (such as a sed) (Ex: "Is the quantity less than 10?") what is the safest way? Could looking at the "length" (number of digits) of numbers be a strategy? | Metin tabanlı bir araçta (sed gibi) sayısal büyüklük karşılaştırması yapmanın (Örn: "Miktar 10'dan küçük mü?") en güvenli yolu nedir? Rakamların "uzunluğuna" (basamak sayısına) bakmak bir strateji olabilir mi? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee '/stock:[[:space:]]+[0-9]{1}[[:space:]]+/I s/^/\[CRITICAL\] /g; \
/critical/I s/REORDER: NO/REORDER: YES/g; \
s/stock: 0/OUT_OF_STOCK/Ig' g37_inventory.txt \
| sed -E 's/STOCK: 9{1}[[:space:]]/STOCK: 10/g'
```
