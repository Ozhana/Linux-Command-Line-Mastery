# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: Your robot receives data from 3 different sensors (Distance, Speed, Temperature) while moving. The log format is a bit “scattered”: <br> [SAAT] SENSOR_TIPI:DEGER (UNIT) STATUS <br><br> Example line: [14:10:05] DIST:45.2 (cm) ACTIVE | SENARYO: Robotun hareket halindeyken 3 farklı sensörden (Mesafe, Hız, Sıcaklık) veri alıyor. Log formatı biraz "dağınık": <br> [SAAT] SENSOR_TIPI:DEGER (UNIT) STATUS <br> Örnek satır: [14:10:05] DIST:45.2 (cm) ACTIVE |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only DIST (Distance) and TEMP Find rows containing (temperature) sensors. (SPEED ignore your sensor). <br><br> 2. Status from these lines ACTIVE filter what happened. <br><br>3. Challenging Part: Distance data 50.0 which is greater than cm (with Regex: [5-9][0-9]\.[0-9]) OR Temperature data 30.0 the one greater than degree (3[0-9]\.[0-9]) capture rows. <br><br>4. Just in printout [SAAT] and the DEGER show part (Tip: cut pay attention to space and two points when using) | 1. Sadece DIST (Mesafe) ve TEMP (Sıcaklık) sensörlerini içeren satırları bul. (SPEED sensörünü görmezden gel). <br><br> 2. Bu satırlar arasından durumu ACTIVE olanları süz. <br><br> 3. Zorlayıcı Kısım: Mesafe verisi 50.0 cm'den büyük olan (Regex ile: [5-9][0-9]\.[0-9]) VEYA Sıcaklık verisi 30.0 dereceden büyük olan (3[0-9]\.[0-9]) satırları yakala. <br><br> 4. Çıktıda sadece [SAAT] ve DEGER kısmını göster (İpucu: cut kullanırken boşluk ve iki noktaya dikkat). |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -Ei "DIST|TEMP" g17_telemetry.log
2. grep -Ei "DIST|TEMP" g17_telemetry.log | grep -i "ACTIVE"
3. grep -Ei "DIST|TEMP" g17_telemetry.log | grep -i "ACTIVE" | grep -E "DIST:[5-9][0-9].[0-9]|TEMP:[3-9][0-9].[0-9]"
4. grep -Ei "DIST|TEMP" g17_telemetry.log | grep -i "ACTIVE" | grep -E "DIST:[5-9][0-9].[0-9]|TEMP:[3-9][0-9].[0-9]" | cut -d' ' -f1,2
```
