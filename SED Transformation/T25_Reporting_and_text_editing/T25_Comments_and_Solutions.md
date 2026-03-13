# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: Bu uygulamayla yeteneklrimizi master seviyesine cikaracagiz |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| Analytical Question: | Analitik Soru: |
|  | Bir veri analisti olarak; sed'in bu "hızlı ve hafif" düzenleme gücü mü, yoksa pandas'ın o "ağır ama detaylı" analiz gücü mü projelerinizde daha kritik? İkisini hangi senaryolarda tercih edersiniz? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi |
|  | Sed: Bir cerrahın neşteri gibidir. Hafiftir, hızlıdır, sisteme yük bindirmez. GB'larca büyüklükteki bir log dosyasını, dosyayı belleğe (RAM) yüklemeden satır satır işleyip temizleyebilir. Veri analizi öncesi "ön temizlik" (pre-processing) için rakipsizdir.<br><br> Pandas: Bir laboratuvar gibidir. Veriyi belleğe alır, satırlar arası ilişkileri inceler, istatistiksel modeller kurar. |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Düşük Öncelikli Veriyi Temizle: Dosyadaki LEVEL: Low içeren tüm satırları tamamen silin (d). <br><br> 2. ID Formatını Değiştir: ID-123 olan kısımları [ISSUE_#123] yapın. (Back-reference \1 kullanın). <br><br> 3. Hassas Veri Etiketi: Satır başındaki SCAN_DATE: ibaresini silin ancak tarihin hemen yanına (CONFIDENTIAL) ibaresini ekleyin. <br><br> 4. Cerrahi Blok İşlemi (Crest): --- SCAN START --- ve --- SCAN END --- satırları arasındaki (bu satırlar dahil değil) tüm metni BÜYÜK HARFE çevirin. <br> İpucu: /START/,/END/ aralığını kullanın ve \U bayrağı ile & (eşleşen her şey) operatörünü birleştirin. <br><br> 5. Dosya ile Çalışma: Tüm bu komutları final_report.sed isimli bir dosyaya alt alta yazın ve sed -E -f final_report.sed g25_security_scan.txt komutuyla çalıştırarak çıktıyı executive_summary.txt dosyasına yönlendirin. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
A.
sed -Ee '/LOW/Id' -e 's/ID-([0-9]{1,4})/'\['ISSUE_#\1'\]'/' -e 's/SCAN_DATE: /\(CONFIDENTIAL\)/' -e '/^--- SCAN START ---$/,/^--- SCAN END ---$/ { /^--- SCAN START ---$/b; /^--- SCAN END ---$/b; s/.*/\U&/ }' g25_security_scan.txt
```

``` bash
# sed file;
# 1. Low seviyeli bulguları sil
/LOW/Id

# 2. ID formatını değiştir (Tırnak kullanma, doğrudan köşeli parantez yaz)
s/ID-([0-9]{1,3})/[ISSUE_#\1]/

# 3. SCAN_DATE kısmını temizle ve yanına notu ekle
s/SCAN_DATE: ([0-9/]+)/\1 (CONFIDENTIAL)/

# 4. START ve END arasındaki her şeyi büyük harfe çevir
/^--- SCAN START ---$/,/^--- SCAN END ---$/ {
    /^--- SCAN START ---$/b
    /^--- SCAN END ---$/b
    s/.*/\U&/
}
```
