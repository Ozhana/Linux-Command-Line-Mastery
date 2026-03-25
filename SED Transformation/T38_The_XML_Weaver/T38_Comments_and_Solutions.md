# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: You have a syllabus or student list outline (g38_raw_data.txt).<br>Format: CLASS: [SINIF] \| STUDENT: [NAME] \| GRADE: [SCORE] | SENARYO: bu görevde sed'i bir "Code Generator" (Kod Üretici) olarak kullanacağız. Elimizde düz bir metin dosyası var ama biz bunu hiyerarşik bir XML/HTML yapısına dönüştüreceğiz. <br><br>Elinizde bir ders programı veya öğrenci listesi taslağı var (g38_raw_data.txt). <br><br>Format: CLASS: [SINIF] \| STUDENT: [NAME] \| GRADE: [SCORE] |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Tag Creation: Insert each line into the structure:<br>\<record class="[SINIF]"><name>[NAME]</name><score>[SCORE]</score></record> <br><br>2. Conditional Coloring (Logic): If GRADE If 90 or above, the <score> your label \<score status="EXCELLENT"> change to. <br><br>3. Cleaning: In the original line \| and word tags (STUDENT:, the GRADE:) destroy completely.<br><br>4. Challenging Part (Multi-line): To the very beginning of the file <database> and to the very end </database> add tags. (Hint: 1i and the $a remember commands). | 1. Tag Oluşturma: Her satırı şu yapıya sokun:<br>\<record class="[SINIF]"><name>[NAME]</name><score>[SCORE]</score></record><br><br>2. Koşullu Renklendirme (Logic): Eğer GRADE 90 ve üzerindeyse, <score> etiketini \<score status="EXCELLENT"> olarak değiştirin. <br><br>3. Temizlik: Orijinal satırdaki \| ve kelime etiketlerini (STUDENT:, GRADE:) tamamen yok edin.<br><br>Zorlayıcı Kısım (Multi-line): Dosyanın en başına <database> ve en sonuna </database> etiketlerini ekleyin. (İpucu: 1i ve $a komutlarını hatırlayın). |
| Golden Information: | Altin Bilgi: |
| 90-100 to catch up 9[0-9] or 100 you should consider the possibilities. Besides 1i (add to first line) and $a (add to last line) commands, sedthese are the rare and powerful moments when ‘ interferes with file integrity | 90-100 arasını yakalamak için 9[0-9] veya 100 ihtimallerini düşünmelisiniz. Ayrıca 1i (ilk satıra ekle) ve $a (son satıra ekle) komutları, sed'in dosya bütünlüğüne müdahale ettiği nadir ve güçlü anlardır. |
| Analytical Question: | Analitik Soru: |
| When converting a data into a hierarchical structure such as XML, regex groups (\1, the \2How does scrambling the order of ) break the "semantic (semantic) integrity" of the data? sed can you make a "validation" (verification) here, or is all responsibility in your regex writing? | Bir veriyi XML gibi hiyerarşik bir yapıya dönüştürürken, regex gruplarının (\1, \2) sırasını karıştırmak verinin "anlamsal (semantic) bütünlüğünü" nasıl bozar? sed burada bir "validation" (doğrulama) yapabilir mi, yoksa tüm sorumluluk sizin regex yazımınızda mıdır? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee '1i<database>' -e 's/CLASS: ([^ ]+) \| STUDENT: ([^ ]+) \| \
GRADE: ([0-9]+)/<record class="\1"><name>\2<\/name><score>\3<\/score>\
<\/record>/' -e 's/score>9[0-9]/score status="EXCELLENT">9[0-9]/' \
-e 's/score>100/score status="EXCELLENT">100/' -e '$a<\/database>' \
g38_raw_data.txt
```
