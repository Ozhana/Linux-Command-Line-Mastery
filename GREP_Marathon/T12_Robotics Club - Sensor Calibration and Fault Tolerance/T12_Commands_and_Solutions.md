# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: You use a distance sensor (HC-SR04) with Arduino. The sensor sometimes produces nonsense values due to interference in the environment. In your hand g12_sensor_raw.log has file. Format: Timestamp,Distance_cm.

Distance value 400.0 cm with 2.0 cm must be in between. Values other than this are considered "noise" (noise). | SENARYO:  |
| **Step 1:** Prepare the data (or download from here). This is Python code for you g12_sensor_raw.log it will create the file.| **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Find incorrect (Outlier) values: <br> Its distance 3 digit (100.0 and above) of which OR at the beginning minus (-) find lines with signs. <br><br> 2. Extract Clean Data: <br> After eliminating incorrect values, just 2 digit Safe measurements of (between 10.0 and 99.9) g12_temiz_sensor.txt save to file. <br><br> 3. Bonus: Calculate how many clean measurements there are and how many incorrect measurements there are. |  |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash

```
