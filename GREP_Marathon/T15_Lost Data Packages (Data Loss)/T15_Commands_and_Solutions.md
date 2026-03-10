# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4/5 | ***### Zorluk duzeyi:*** 4/5|
| SCENARIO: Sending data over the robot’s Wi-Fi. Packets have a sequence number at the beginning (ID:001, the ID:002...). However, when the connection is lost, some numbers are skipped. As a data analyst, you need to find out at what interval you lost data. | SENARYO: Robotun Wi-Fi üzerinden veri gönderiyor. Paketlerin başında bir sıra numarası var (ID:001, ID:002...). Ancak bağlantı koptuğunda bazı numaralar atlıyor. Veri analisti olarak hangi aralıkta veri kaybı yaşadığını bulman lazım. |
| **Step 1:** Prepare the data (or download from here). This is Python code g15_wifi_packets.log it will create the file. Attention: Some IDs are missing! | **Adım 1:** Data Olustur (veya buradan indir). Bu Python kodu g15_wifi_packets.log dosyasını oluşturacak. Dikkat: Bazı ID'ler eksik! |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Find Signal Strength (RSSI) Weak Ones: Signal strength -70dBmworse than (i.e. -7[0-9] or -8[0-9]Find all rows with ). <br><br> 2. List IDs Only: These are just weakly connected packages ID:XXX press the parts on the screen. <br><br> 3. Mathematical Logic Question: But if you are expecting 100 packages in total wc -l how do you assign the number of lost packets to a Bash variable if it gives you 88 lines? | 1. Sinyal Gücü (RSSI) Zayıf Olanları Bul: Sinyal gücü -70dBm'den daha kötü (yani -7[0-9] veya -8[0-9]) olan tüm satırları bul. <br><br> 2. Sadece ID'leri Listele: Bu zayıf bağlantılı paketlerin sadece ID:XXX kısımlarını ekrana bas. <br><br> 3. Matematiksel Mantık Sorusu: Eğer toplamda 100 paket bekliyorsan ama wc -l sana 88 satır veriyorsa, kayıp paket sayısını bir Bash değişkenine nasıl atarsın? |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
beklenen=100
gelen=$(grep -c "ID:" g15_wifi_packets.log)
kayip=$((beklenen - gelen))
echo "Kayıp paket sayısı: $kayip"
```
