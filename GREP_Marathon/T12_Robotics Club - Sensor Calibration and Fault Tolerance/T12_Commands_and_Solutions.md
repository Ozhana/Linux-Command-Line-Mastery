# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: You use a distance sensor (HC-SR04) with Arduino. The sensor sometimes produces nonsense values due to interference in the environment. In your hand g12_sensor_raw.log has file. Format: Timestamp,Distance_cm. <br><br> Distance value 400.0 cm with 2.0 cm must be in between. Values other than this are considered "noise" (noise). | SENARYO: Arduino ile bir mesafe sensörü (HC-SR04) kullanıyorsun. Sensör bazen çevredeki parazitlerden dolayı saçma sapan değerler üretiyor. Elinde g12_sensor_raw.log dosyası var. Format: Timestamp,Distance_cm. <br><br> Mesafe değeri 2.0 cm ile 400.0 cm arasında olmalı. Bunun dışındaki değerler "gürültü" (noise) kabul ediliyor |
| **Step 1:** Prepare the data (or download from here). This is Python code for you g12_sensor_raw.log it will create the file.| **Adım 1:** Data Olustur (veya buradan indir). Bu Python kodu sana g12_sensor_raw.log dosyasını oluşturacak. |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Find incorrect (Outlier) values: <br> Its distance 3 digit (100.0 and above) of which OR at the beginning minus (-) find lines with signs. <br><br> 2. Extract Clean Data: <br> After eliminating incorrect values, just 2 digit Safe measurements of (between 10.0 and 99.9) g12_temiz_sensor.txt save to file. <br><br> 3. Bonus: Calculate how many clean measurements there are and how many incorrect measurements there are. | 1. Hatalı (Outlier) değerleri bul: <br> Mesafesi 3 haneli (100.0 ve üzeri) olan VEYA başında eksi (-) işareti olan satırları bul. <br><br> 2. Temiz Veri Çıkar: <br> Hatalı değerleri eledikten sonra, sadece 2 haneli (10.0 ile 99.9 arası) olan güvenli ölçümleri g12_temiz_sensor.txt dosyasına kaydet. <br><br> 3. Bonus: Kaç adet temiz ölçüm, kaç adet hatalı ölçüm olduğunu hesapla. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -E "^[^,]+,[0-9]{3}|-" g12_sensor_raw.log
2. grep -E "^[^,]+,[0-9]{2}" g12_sensor_raw.log |tee /dev/stderr | wc -l
3. echo -e "Toplamda\n $(grep -Ec "^[^,]+,[0-9]{3}|-" g12_sensor_raw.log)  hatali sonuc\n $(grep -Ec "^[^,]+,[0-9]{2}" g12_sensor_raw.log)  10'dan buyuk sonuc\n $(grep -Ec "^[^,]+,[0-9]{1}" g12_sensor_raw.log)  adet 10'dan kucuk sonuc var"
```
All together
``` bash
echo -e " Tum Temiz Sonuclar ------\n$(grep -vE "^[^,]+,[0-9]{3}|-" g12_sensor_raw.log)\n Hepsi toplam  $(grep -vEc "^[^,]+,[0-9]{3}|-" g12_sensor_raw.log)  adet.\n10'dan buyuk olanlar : $(grep -Ec "^[^,]+,[0-9]{2}" g12_sensor_raw.log)\n10'dan Kucuk olalar : $(grep -Ec "^[^,]+,[0-9].[0-9]" g12_sensor_raw.log) adet"
```
