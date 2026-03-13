# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: Bu uygulamayla yeteneklrimizi master seviyesine cikaracagiz |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Düşük Öncelikli Veriyi Temizle: Dosyadaki LEVEL: Low içeren tüm satırları tamamen silin (d). <br><br> 2. ID Formatını Değiştir: ID-123 olan kısımları [ISSUE_#123] yapın. (Back-reference \1 kullanın). <br><br> 3. Hassas Veri Etiketi: Satır başındaki SCAN_DATE: ibaresini silin ancak tarihin hemen yanına (CONFIDENTIAL) ibaresini ekleyin. <br><br> 4. Cerrahi Blok İşlemi (Crest): --- SCAN START --- ve --- SCAN END --- satırları arasındaki (bu satırlar dahil değil) tüm metni BÜYÜK HARFE çevirin. <br> İpucu: /START/,/END/ aralığını kullanın ve \U bayrağı ile & (eşleşen her şey) operatörünü birleştirin. <br><br> 5. Dosya ile Çalışma: Tüm bu komutları final_report.sed isimli bir dosyaya alt alta yazın ve sed -E -f final_report.sed g25_security_scan.txt komutuyla çalıştırarak çıktıyı executive_summary.txt dosyasına yönlendirin. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
