# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: Your robot receives data from 3 different sensors (Distance, Speed, Temperature) while moving. The log format is a bit “scattered”:
[SAAT] SENSOR_TIPI:DEGER (UNIT) STATUS <br><br> Example line: [14:10:05] DIST:45.2 (cm) ACTIVE | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only DIST (Distance) and TEMP Find rows containing (temperature) sensors. (SPEED ignore your sensor). <br><br> 2. Status from these lines ACTIVE filter what happened. <br><br>3. Challenging Part: Distance data 50.0 which is greater than cm (with Regex: [5-9][0-9]\.[0-9]) OR Temperature data 30.0 the one greater than degree (3[0-9]\.[0-9]) capture rows. <br><br>4. Just in printout [SAAT] and the DEGER show part (Tip: cut pay attention to space and two points when using) |  |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash

```
