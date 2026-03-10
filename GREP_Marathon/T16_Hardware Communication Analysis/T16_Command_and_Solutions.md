# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: A new sensor module in the robotics club sends data via a binary (binary) protocol. In the log file, each line is of the following format: SENSOR_ID: [8-BIT_DATA] [CHECKSUM]. <br> To calculate the margin of error of the processor (Arduino/ESP32), you need to find lines in the data that have a specific bit sequence and do not contain checksum errors. | SENARYO: Robotics kulübündeki yeni bir sensör modülü, verileri ikili (binary) bir protokol ile gönderiyor. Log dosyasında her satır şu formattadır: SENSOR_ID: [8-BIT_DATA] [CHECKSUM]. <br> İşlemcinin (Arduino/ESP32) hata payını hesaplamak için, verinin içinde spesifik bir bit dizilimi olan ve checksum hatası içermeyen satırları bulman gerekiyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. At least three in a row 1 (that is 111Find 8-bit data packets located in ). <br><br> 2. From these packages, finally ERR (Checksum error) written by ele (Display). <br><br> 3. Just the valid packages you found SENSOR_ID parts (ID_XXX get it in format), sort them alphabetically, and report how many "valid data" came from each ID. | 1. İçinde ardışık en az üç tane 1 (yani 111) bulunan 8 bitlik veri paketlerini bul. <br><br> 2. Bu paketlerin içinden, sonunda ERR (Checksum hatası) yazanları ele (Gösterme). <br><br> 3. Bulduğun geçerli paketlerin sadece SENSOR_ID kısımlarını (ID_XXX formatında) al, bunları alfabetik sıraya diz ve her ID'den kaç tane "geçerli veri" geldiğini raporl |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -E "111" g16_hardware.log
2. grep -E "111" g16_hardware.log | grep -iv "err"
3. grep -E "111" g16_hardware.log | grep -iv "err" | sort -k1r | grep -Eo ^"[^:]+" | uniq -c
```
