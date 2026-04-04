# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 8/10 | ***### Zorluk duzeyi:*** 8/10|
| SCENARIO:  | SENARYO: Bir e-ticaret sitesinin loglarını analiz ediyorsun. Elinde /urun/laptop?id=101 veya /kategori/elektronik?sayfa=2 gibi karmaşık URL'ler var. Patronun (veya meraklı bir veri analisti olarak sen), sorgu parametrelerini (? işaretinden sonrasını) çöpe atıp, sadece ana dizinlerin (Path) kaçar kez ziyaret edildiğini görmek istiyorsun. Ayrıca "404 Not Found" hatası veren sayfaların bir listesini tutmalısın. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. URL Shredding: Column 4 in the log file (URL part) split() with function ? split from. Just take the cleared path (path).<br><br>2. Statistics: Each cleaned path (Ex: /urun/laptop) keep in an array how many times you've been visited (hit[path]++).<br><br>3. Error Tracking: Status code (last column) 404 find the rows that are present and store them in an array as unique (unique) from which IPs these errors come.<br><br>4. Sorting (Master's Job): END present a report in order from the most visited page to the least on your block. (What we learned in the previous lesson | "sort -rnk2" don't forget to use your structure!)<br><br>5. Summary Report: Print the total number of “Successful (200)” and “Inaccurate (404/500)” transactions to the end. | 1. URL Parçalama: Log dosyasındaki 4. sütunu (URL kısmı) split() fonksiyonu ile ? işaretinden böl. Sadece temizlenmiş yolu (path) al.<br><br>2. İstatistik: Temizlenmiş her bir yolun (Örn: /urun/laptop) kaç kez ziyaret edildiğini bir dizide tut (hit[path]++).
<br><br>3. Hata Takibi: Durum kodu (son sütun) 404 olan satırları bul ve bu hataların hangi IP'lerden geldiğini benzersiz (unique) olarak bir dizide sakla.<br><br>4. Sıralama (Usta İşi): END bloğunda en çok ziyaret edilen sayfadan en aza doğru sıralı bir rapor sun. (Önceki derste öğrendiğimiz | "sort -rnk2" yapısını kullanmayı unutma!)<br><br>5. Özet Rapor: En sona toplam "Başarılı (200)" ve "Hatalı (404/500)" işlem sayılarını yazdır. |
| Golden Information: | Altin Bilgi: |
| In AWK tolower() and the toupper() converting URLs to lowercase using their functions (so that "Search" and "search" are considered the same) and analyzing them is always a healthier "Normalize" process. | AWK'da tolower() ve toupper() fonksiyonlarını kullanarak URL'leri küçük harfe çevirip ("Search" ve "search" aynı sayılsın diye) analiz etmek her zaman daha sağlıklı bir "Normalize" işlemidir. |
| Analytical Question: | Analitik Soru: |
| If more than one URL ? or & if so split() how would the function fill the array? | Eğer bir URL içinde birden fazla ? veya & olsaydı, split() fonksiyonu diziyi nasıl doldururdu? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
