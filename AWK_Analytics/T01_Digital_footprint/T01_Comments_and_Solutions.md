# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 6/10 | ***### Zorluk duzeyi:*** 6/10|
| SCENARIO:  | SENARYO: Bu görevde AWK'ın temel sütun mantığını ve BEGIN/END bloklarını kullanacağız. <br><br>Bir freelance platformunun veri analistisin. Elinde platformdaki kullanıcıların hareketlerini içeren karmaşık bir log dosyası var. Bu dosyada kullanıcı ID'si, işlem tipi, kazanç, işlem süresi ve platforma giriş yaptığı cihaz bilgisi yer alıyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Sadece PROJECT_COMPLETE olan satırları bul ve kullanıcı ID'si ile kazandığı miktarı ekrana yazdır.<br><br>2. İşlem süresi (duration) 60 dakikadan fazla olan işlemlerin sayısını bul (Hangi değişkeni artırarak sayabilirsin?).<br><br>3. Tüm dosya boyunca toplam amount (kazanç) değerini hesapla ve en sonda END bloğunda yazdır.<br><br>4. Cihaz bilgisi (son sütun) "Fedora_v43" olan satırların sadece ilk 3 karakterini (substr kullanarak) ve satır numarasını yazdır. <br><br>5. Raporlama: Çıktının en başına "FREELANCE FINANSAL RAPOR" başlığını, en sonuna da "TOPLAM ISLEM: [NR]" bilgisini printf kullanarak hizalı şekilde ekle. |
| Golden Information: | Altin Bilgi: |
|  | 1. $1, $2, ... $NF: Alan değişkenleri. $NF her zaman sonuncu sütunu verir.<br><br>NR: (Number of Records) O an işlenen satırın numarası.<br><br>NF: (Number of Fields) O satırdaki toplam sütun sayısı.<br><br>printf: Veriyi hizalı ve profesyonel formatta yazdırmak için (C dilindeki gibi). |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
