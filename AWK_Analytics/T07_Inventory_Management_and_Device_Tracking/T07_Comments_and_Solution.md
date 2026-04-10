# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 8/10 | ***### Zorluk duzeyi:*** 8/10|
| SCENARIO: You've set up a new inventory system for the Robotics Club at school. However, unfortunately, the system outputs are in a "block" structure. The ID, name, operating system and status (Active/Repair) of each device are spread over 4-5 lines and between blocks END_RECORD written. <br><br>From you, just treat these blocks as if they were a single "line" Fedora using and Active I want you to report any devices that are present. | SENARYO: Okuldaki Robotics Club için yeni bir envanter sistemi kurdun. Ancak sistem çıktıları maalesef "blok" yapısında. Her cihazın ID'si, adı, işletim sistemi ve durumu (Aktif/Tamirde) 4-5 satıra yayılmış durumda ve bloklar arasına END_RECORD yazılmış.<br><br>Senden, bu blokları tek bir "satırmış gibi" ele alıp sadece Fedora kullanan ve Aktif olan cihazları raporlamanı istiyorum. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. RS Setting: BEGIN on your blog RS (Record Separator) value "END_RECORD\n" set to.<br><br>2. FS Setting: To see each row within the block as a column (Field) FS your value "\n" (line break) do.<br><br>3. Filtering: If in the record (block) "Fedora" AND THE "Active" if the words are mentioned, process that block.<br><br>4. Released Clean: Put the ID and name of the device you found side by side, between them (\tPrint by putting ).<br><br>5. Summary: END report how many "Fedora" devices you found in total on your blog. | 1. RS Ayarı: BEGIN bloğunda RS (Record Separator) değerini "END_RECORD\n" olarak ayarla.<br><br>2. FS Ayarı: Blok içindeki her satırı bir sütun (Field) olarak görmek için FS değerini "\n" (satır sonu) yap.<br><br>3. Filtreleme: Eğer kayıt (blok) içinde "Fedora" VE "Aktif" kelimeleri geçiyorsa o bloğu işle.<br><br>4. Temiz Çıktı: Bulduğun cihazın ID'sini ve adını yan yana, aralarına tab (\t) koyarak yazdır.<br><br>5. Özet: END bloğunda toplam kaç adet "Fedora" cihazı bulduğunu raporla. |
| Golden Information: | Altin Bilgi: |
| RS = "" (Empty RS) is a special mode. in this case, AWK accepts consecutive empty lines as separators. It is known as "paragraph mode" and saves lives when analyzing unstructured text files. | RS = "" (Empty RS) özel bir moddur. AWK bu durumda ardışık gelen boş satırları ayırıcı kabul eder. "Paragraf modu" olarak bilinir ve yapılandırılmamış metin dosyalarını analiz ederken hayat kurtarır. |
| Analytical Question: | Analitik Soru: |
| If RS if you leave its value completely blank (RS = ""), How does AWK behave? | RS değerini tamamen boş bırakırsan (RS = ""), AWK nasıl bir davranış sergiler? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
awk '
BEGIN { 
    RS = "END_RECORD\n"; 
    FS = "\n"; 
    printf "%-10s | %-20s\n", "ID", "CIHAZ ADI";
    print "-----------------------------------";
    fed_count = 0 
}
{
    # Filtreleme: 3. satır Fedora içeriyor mu VE 4. satır Aktif mi?
    if ($3 ~ /Fedora/ && $4 ~ /Aktif/) {
        fed_count++;
        split($1, id_arr, ": ");
        split($2, cihaz_arr, ": ");
        printf "%-10s | %-20s\n", id_arr[2], cihaz_arr[2];
    }
}
END { 
    print "-----------------------------------";
    print "Toplam Aktif Fedora Cihazı: " fed_count 
}' g07_inventory.txt
```
