# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: You have a system error report (g29_system.log). In this file sometimes "System Status" (STATUS: ...) sometimes "Mistakes" (ERROR: ...) writes. What is requested from you; last seen STATUS keep your knowledge in mind and keep it in mind ERROR create a report that adds the current status to the beginning of the line. | SENARYO: Elinizde bir sistemin hata raporu var (g29_system.log). Bu dosyada bazen "Sistem Durumu" (STATUS: ...) bazen de "Hatalar" (ERROR: ...) yazıyor. Sizden istenen; en son görülen STATUS bilgisini aklında tutup, her ERROR satırının başına o anki statusü ekleyen bir rapor oluşturmanız. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Using Hold Space (h, the g, the x): * h (Hold): Copies the pattern space into the drawer.<br><br>g(Get): Returns what's in the drawer to pattern space. <br><br>2. Logic: In line STATUS if it does pass, throw it in the drawer (h). In line ERROR if it does, take the status in the drawer with you (G) and combine the two in one line.<br><br>3. Cleaning: Print only lines containing ERROR (with status next to it).<br><br>4. Format: The output should be like this: [Current Status: OK] -> ERROR: Database_Timeout <br><br>5. Filter: Do not report (delete) errors with "Low" in them. | 1. Hold Space Kullanımı (h, g, x): * h (Hold): Pattern space'i çekmeceye kopyalar. <br><br>g (Get): Çekmecedekini pattern space'e geri getirir. <br><br>2. Mantık: Satırda STATUS geçiyorsa, onu çekmeceye at (h). Satırda ERROR geçiyorsa, çekmecedeki statusü yanına al (G) ve ikisini tek satırda birleştir.<br><br>3. Temizlik: Sadece ERROR içeren (yanında statusü ile birlikte) satırları yazdırın.<br><br>4. Format: Çıktı şu şekilde olmalı: [Current Status: OK] -> ERROR: Database_Timeout<br><br>5. Filtre: İçinde "Low" geçen hataları raporlamayın (silin). |
| Golden Information: | Altin Bilgi: |
| sed -n '/STATUS/h; /ERROR/ { G; s/\n/ /; p }' <br><br>This pattern; It memorizes the STATUS line, and when it sees ERROR, it pastes the line in memory under it (G), then the line break in between (\n) replaces with a space and prints. | sed -n '/STATUS/h; /ERROR/ { G; s/\n/ /; p }' <br><br>Bu kalıp; STATUS satırını belleğe alır, ERROR gördüğünde bellekteki satırı altına yapıştırır (G), sonra aradaki satır sonunu (\n) boşlukla değiştirip yazdırır. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -n '/STATUS/h; /ERROR/{G; s/^\(.*\)\n\(.*\)$/[\2] -> \1/p}' g29_system.log | sed '/STATUS/!d'
```
