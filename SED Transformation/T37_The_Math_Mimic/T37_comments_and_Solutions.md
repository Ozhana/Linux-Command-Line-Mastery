# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: sed aslında sayıları toplama veya çıkarma yeteneğine sahip değildir (çünkü her şeyi metin/string olarak görür). Ancak biz sed'i karakter bazlı bir hesap makinesine dönüştürebiliriz. <br><br>Bir envanter listeniz var (g37_inventory.txt). Bazı ürünlerin stokları kritik seviyeye düşmüş. <br><br>Format: PROD_ID: [ID] \| STOCK: [QTY] \| REORDER: [YES/NO] |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Stok Kontrolü: Eğer STOCK değeri tek haneliyse (0-9), bu ürünün yanına [CRITICAL] ibaresini ekleyin. <br><br>2. Otomatik Sipariş: Eğer stok CRITICAL ise, REORDER: NO kısmını REORDER: YES olarak değiştirin. <br><br>3. Sayısal Dönüşüm (Zor Kısım): Stokta 0 (sıfır) gördüğünüz her yere metin olarak OUT_OF_STOCK yazın. <br><br>4. Bonus (Zihni Sinir): Sadece sed kullanarak, STOCK: 9 olanları STOCK: 10 yapabilir misiniz? (İpucu: Sayısal toplama yapamazsınız, sadece s/9/10/ gibi bir metin değişimi yapmalısınız). |
| Golden Information: | Altin Bilgi: |
|  | STOCK: 9'u 10 yaparken dikkatli olun; eğer STOCK: 19 varsa onu da 110 yapabilirsiniz! Bu yüzden regex'te kelime sınırlarını ([[:space:]] veya \| işaretini) çapa olarak kullanmalısınız. |
| Analytical Question: | Analitik Soru: |
|  | Metin tabanlı bir araçta (sed gibi) sayısal büyüklük karşılaştırması yapmanın (Örn: "Miktar 10'dan küçük mü?") en güvenli yolu nedir? Rakamların "uzunluğuna" (basamak sayısına) bakmak bir strateji olabilir mi? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee '/stock:[[:space:]]+[0-9]{1}[[:space:]]+/I s/^/\[CRITICAL\] /g; /critical/I s/REORDER: NO/REORDER: YES/g; s/stock: 0/OUT_OF_STOCK/Ig' g37_inventory.txt | sed -E 's/STOCK: 9{1}[[:space:]]/STOCK: 10/g'
```
