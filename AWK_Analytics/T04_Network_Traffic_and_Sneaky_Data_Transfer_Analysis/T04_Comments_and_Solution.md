# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 7.5/10 | ***### Zorluk duzeyi:*** 7.5/10|
| SCENARIO: You are examining the network logs of the Fedora server. He has a huge file on which IP address he transfers, at what time, and how much data (in Bytes). But there is a problem: The same IP address traded hundreds of times during the day. Your mission, every IP total how much data it consumes and how many times finding that you are connecting. | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Array Setup: Using each IP address as the "key" (key), add up the total amount of Bytes that IP transferred in an array.<br><br>2. Connection Counter: How many times the same IP connects (number of rows) in a second array (count[ip]++ hold it).<br><br>3. MB Conversion: END byte values when printing results in the block MegaByte (MB) convert to type (1 MB = 1,048,576 Bytes).<br><br>4. Loop Usage: END to print the array in your block, you must use the following structure:<br><br>for (ip in total_size) { print ip, total_size[ip] }<br><br>5. Anomaly Detection: If an IP address in total More than 5 MB if he transferred data, take it with him "[HIGH TRAFFIC]" put warning. | 1. Dizi Kurulumu: Her IP adresini "anahtar" (key) olarak kullanarak, o IP'nin toplam transfer ettiği Byte miktarını bir dizide topla.<br><br>2. Bağlantı Sayacı: Aynı IP'nin kaç kez bağlantı kurduğunu (satır sayısını) ikinci bir dizide (count[ip]++ şeklinde) tut.<br><br>3. MB Dönüşümü: END bloğunda sonuçları yazdırırken Byte değerlerini MegaByte (MB) cinsine çevir (1 MB = 1.048.576 Byte).<br><br>4. Döngü Kullanımı: END bloğunda diziyi yazdırmak için şu yapıyı kullanmalısın:<br><br>for (ip in total_size) { print ip, total_size[ip] }<br><br>5. Anomali Tespiti: Eğer bir IP adresi toplamda 5 MB'dan fazla veri transfer ettiyse, yanına "[YÜKSEK TRAFİK]" uyarısı koy. |
| Golden Information: | Altin Bilgi: |
| AWK sequences are "unordered" by default. They may come in a different order each time you press the screen. For a sequential report END print command in the block \| "sort -nk2" it is the fastest way to bypass it to the Linux terminal. | AWK dizileri varsayılan olarak "sırasızdır". Ekrana her bastığında farklı bir sırayla gelebilirler. Sıralı bir rapor için END bloğundaki print komutunu \| "sort -nk2" şeklinde Linux terminaline paslamak en hızlı yoldur. |
| Analytical Question: | Analitik Soru: |
| If you want to sort the data in the array alphabetically by smallest to largest or IP address, AWK asort() or asorti() can you use its functions? Otherwise, the output is a pipe (\|) with Linux sort should you send it to your command? | Dizideki verileri küçükten büyüğe veya IP adresine göre alfabetik sıralamak istersen AWK'nın asort() veya asorti() fonksiyonlarını kullanabilir misin? Yoksa çıktıyı bir pipe (\|) ile Linux'un sort komutuna mı göndermelisin? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
{
    # $2 IP adresi, $NF (en sondaki) Byte miktarı
    byte[$2] += $3
    count[$2]++
}

END {
    printf "%-18s | %-15s | %-10s | %-8s\n", "DURUM", "IP ADRESI", "TRAFIK(MB)", "ADET"
    print "----------------------------------------------------------------------"
    
    for (ip in byte) {
        mb = byte[ip] / 1048576
        # 5 MB üzeri alarm (Senin 9 MB mantığını 5'e çektim hocam)
        uyari = (mb >= 5) ? "[YUKSEK TRAFIK]" : "[NORMAL]"
        
        printf "%-18s | %-15s | %-10.2f | %-8d\n", uyari, ip, mb, count[ip] | "sort -nk3"
    }
}
```
