# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: You have a very dirty file (g32_dirty_data.csv). At the beginning and end of the lines, there are endless “garbage” characters (dots, commas, dashes, spaces) no matter how many times you clear them. s/^[ ,.-]+//g sometimes, in complex arrays (for example, a dot after a gap, and a gap after a dot), it may not be able to clear them all at once | SENARYO: Elinizde çok kirli bir dosya var (g32_dirty_data.csv). Satırların başında ve sonunda, ne kadar temizlerseniz temizleyin bitmeyen "çöp" karakterler (nokta, virgül, tire, boşluk) var. s/^[ ,.-]+//g bazen karmaşık dizilimlerde (örneğin boşluktan sonra nokta, noktadan sonra yine boşluk gelmesi gibi) tek seferde hepsini temizleyemeyebilir |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Define Tag: :temizle select a starting point named.<br><br>2. Surgical Cleaning: At the beginning of the line (^) and at the end ($) all  , the ., the ,, the - one character s/// delete with.<br><br>3. Loop Setup (The Branch): t temizle use command. (This command means: "If you just deleted something, go back to the beginning and look again").<br><br>4. Conclusion: Until the line becomes completely smooth sed it will spin within itself and when it is finished, it will be in its clean state.<br><br>5. Filter: If the line is completely empty when cleaning is finished, do not print that line. | 1. Etiket Tanımlayın: :temizle adında bir başlangıç noktası seçin. <br><br>2. Cerrahi Temizlik: Satırın başındaki (^) ve sonundaki ($) tüm  , ., ,, - karakterlerini tek bir s/// ile silin. <br><br>3. Döngü Kur (The Branch): t temizle komutunu kullanın. (Bu komut: "Eğer az önce bir şey sildiysen, başa dön ve bir daha bak" demektir). <br><br>4. Sonuç: Satır tamamen pürüzsüz hale gelene kadar sed kendi içinde dönecek, bittiğinde tertemiz halini basacaktır. <br><br>5. Filtre: Eğer temizlik bittiğinde satır tamamen boş kalmışsa, o satırı yazdırmayın. |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
| As a data analyst; Why is it safer to do a little cleaning and set up a loop that says "go back to square one until everything is clear" instead of writing a single giant regex? What does the cycle give us in complex and unpredictable dirty data? | Bir veri analisti olarak; neden tek bir devasa regex yazmak yerine, küçük bir temizlik yapıp "her şey temizlenene kadar başa dön" diyen bir döngü kurmak daha güvenlidir? Karmaşık ve öngörülemez kirli verilerde döngü bize ne kazandırır? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
| What I ask is "Why loop instead of a single regex?" the answer to the question is <br><br>**"Unpredictable Layers"**. <br><br>Let's say your data is like this:  ...- -...DATA...- -... <br><br>A single global regex (s/^[ .-]+//gWhen you type ), the regex engine looks at the beginning of the line, deletes the matching group, and stops. If under the deleted part new one if the dirty layer appears (for example, new spots that appear after the gaps are erased), a standard s/// sometimes you may miss these or it requires you to write a very complex regex. | Sorduğum "Neden tek bir regex yerine döngü?" sorusunun cevabı **"Öngörülemez Katmanlar"**dır. <br><br>Diyelim ki veriniz şöyle:  ...- -...DATA...- -...  <br><br>Tek bir global regex (s/^[ .-]+//g) yazdığınızda, regex motoru satırın başına bakar, eşleşen grubu siler ve durur. Eğer silinen kısmın altından yeni bir kirli katman çıkarsa (örneğin boşluklar silindikten sonra ortaya çıkan yeni noktalar), standart bir s/// bazen bunları kaçırabilir veya çok karmaşık bir regex yazmanızı gerektirir. <br><br>Döngü ise şudur:
"Ben bu yüzeyi bir kez sildim. Bakalım altından hala kir çıkıyor mu? Evet çıkıyor. O zaman bir daha sil. Tertemiz olana kadar devam et!" <br><br>Bu yaklaşım, verinin ne kadar kirli olduğundan bağımsız olarak %100 temizlik garantisi verir. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -En ':temizle; s/[ -.,_]|\b[-,._]\b//g; \
t temizle; /^[[:space:]]+$/d; \
/data/Ip' g32_dirty_data.csv

```
