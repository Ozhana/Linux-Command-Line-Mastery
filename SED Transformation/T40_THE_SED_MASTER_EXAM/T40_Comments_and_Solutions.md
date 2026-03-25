# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: Elinizde çok karmaşık ve "kirli" bir log dosyası (final_exam.log) var. Bu dosya hem kullanıcı verilerini hem de gereksiz sistem çöplerini içeriyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Format Dönüşümü: USER: [name] \| IP: [ip] \| ROLE: [role] satırlarını bulun ve [ROLE] -> [NAME] (IP: [IP]) formatına çevirin. Rol isimlerini tamamen BÜYÜK HARF yapın (\U). <br><br>2. Sayısal Filtreleme: Eğer IP adresi 192. ile başlıyorsa, bu kullanıcıyı "Local" kabul edin ve satırın sonuna [LOCAL_ACCESS] ekleyin.<br><br>3. Çoklu Satır Temizliği: Eğer bir satırda ERROR yazıyor ve bir sonraki satırda CODE: 404 geliyorsa, bu ikiliyi tek bir satırda birleştirin ve başına [CRITICAL_ERR] koyun. <br><br>4. Enjeksiyon: Dosyanın en başına --- START OF AUDIT: [TARİH] --- ve en sonuna --- END OF REPORT --- ekleyin.<br><br>5. Bonus: İçinde TRASH veya DEBUG kelimesi geçen tüm satırları rapordan tamamen imha edin. |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
