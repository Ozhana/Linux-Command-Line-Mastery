# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: There are two different systems in the laboratory: g20_sensor.log (Temperature data) and g20_system.log (System errors). <br> There was a malfunction and we want to find out after which sensor warning this malfunction was triggered. | SENARYO: Laboratuvarda iki farklı sistem var: g20_sensor.log (Sıcaklık verileri) ve g20_system.log (Sistem hataları). <br> Bir arıza oldu ve biz bu arızanın hangi sensör uyarısından sonra tetiklendiğini bulmak istiyoruz. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. g20_system.log the one that gets the "CRITICAL" error in it all hours find (Just take the clock part: 14:20:15 like). <br><br> 2. Challenging Part: In the seconds when these critical error hours pass, g20_sensor.log what is the temperature (TEMP) in his file? <br> Hint: You should assign the hours you found in the first file to a variable and search for that variable in the second file. <br><br> 3. The temperature value from these matching rows 40.0 filter those above the degree. <br><br> 4. Final: Print result in: Kritik Hata Aninda Sicaklik: [SAAT] -> [SICAKLIK] | 1. g20_system.log içinde "CRITICAL" hatası alan tüm saatleri bul (Sadece saat kısmını al: 14:20:15 gibi). <br><br> 2. Zorlayıcı Kısım: Bu kritik hata saatlerinin geçtiği saniyelerde, g20_sensor.log dosyasında sıcaklık (TEMP) kaçmış? <br> İpucu: Birinci dosyadan bulduğun saatleri bir değişkene atayıp, ikinci dosyada o değişkeni aratmalısın. <br><br> 3. Bu eşleşen satırlardan sıcaklık değeri 40.0 derecenin üzerinde olanları süz. <br><br> 4. Final: Sonucu şu formatta yazdır: Kritik Hata Aninda Sicaklik: [SAAT] -> [SICAKLIK] |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -Ei "critical" g20_system.log | grep -Eo "([0-9]{2}:){2}[0-9]{2}"

2. tim=$(!!)

for i in $tim; do grep -E "$i" g20_sensor.log; done
# 1. Saatleri bir listeye alalım
hatali_saatler=$(grep -Ei "critical" g20_system.log | grep -Eo "([0-9]{2}:){2}[0-9]{2}")

# 3 - 4. Döngü ile her saat için sensör verisini çekip formatlayalım
for saat in $hatali_saatler; do
    # Sensör logunda o saati buluyoruz
    sensor_verisi=$(grep "\[$saat\]" g20_sensor.log)
    
    # Sadece 40.0 derece üzerindekileri raporlayalım (Regex: 4[0-9]\.[0-9])
    echo "$sensor_verisi" | grep -E "4[0-9]\.[0-9]" | while read -r satir; do
        sicaklik=$(echo "$satir" | grep -Eo "[0-9]{2}\.[0-9]")
        echo "Kritik Hata Aninda Sicaklik: [$saat] -> $sicaklik C"
    done
done
```
