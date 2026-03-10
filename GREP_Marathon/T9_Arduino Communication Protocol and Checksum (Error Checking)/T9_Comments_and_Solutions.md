# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: At the Robotics club, you report two Arduinos via serial port. The packages come in the following format: START:DATA:CHECKSUM:END. It's just your job data (DATA) consists of 3-digit numbers and the ending with END finding valid packages. | SENARYO: Robotics kulübünde iki Arduino'yu seri port üzerinden haberleştiriyorsun. Paketler şu formatta geliyor: START:DATA:CHECKSUM:END. Senin görevin, sadece verisi (DATA) 3 haneli sayılardan oluşan ve END ile biten geçerli paketleri bulmak. |
| **Step 1:** Prepare the data (or download from here). This is Python code g9_arduino_serial.log it will create the file. | **Adım 1:** Data Olustur (veya buradan indir).Bu Python kodu g9_arduino_serial.log dosyasını oluşturacak. |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only completed (that is :END Find packages ending in). <br> 2. Just among these DATA part is 3 digits filter what happened. <br> 3. Bonus: Show only DATA and CHECKSUM parts of valid packages (Tip: cut -d':' -f2,3). | 1. Sadece tamamlanmış (yani :END ile biten) paketleri bul. <br> 2. Bunların içinden sadece DATA kısmı 3 haneli olanları süz. <br> 3. Bonus: Geçerli paketlerin sadece DATA ve CHECKSUM kısımlarını göster (İpucu: cut -d':' -f2,3). |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |
| grep -E "^[^:]+:[1-9][0-9]{2}" g9_arduino_serial.log \| grep "END" \| cut -d':' -f2,3 | grep -E "^[^:]+:[1-9][0-9]{2}" g9_arduino_serial.log \| grep "END" \| cut -d':' -f2,3 |
