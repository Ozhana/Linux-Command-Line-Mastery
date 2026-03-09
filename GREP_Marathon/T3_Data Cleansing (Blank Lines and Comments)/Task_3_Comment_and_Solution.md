# INSTRUCTIONS IN ENGLISH


# GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| *** ### Difficulty Degree:** 2/5 | *** ### Zorluk duzeyi:*** 2/5|
| Situation: You are working on an Arduino project or have a configuration file. The file is very crowded; dozens of empty lines and # or // There are comment lines starting with. You need to clear this "noise" to see the real code (i.e. useful data). | Durum: Bir Arduino projesi üzerinde çalışıyorsun veya bir konfigürasyon dosyan var. kalabalık; içinde onlarca boş satır ve # veya // ile başlayan yorum satırları var. Gerçek kodu (yani işe yarar veriyi) görmek için bu "gürültüyü" temizlemen gerekiyor. |
| **Step 1:** Prepare Data | **Adım 1:** Veriyi Hazırla |
| This is Python code for you project.ino it will give you a file called, full of spaces and comments. | Bu Python kodu sana project.ino adında, içi boşluklar ve yorumlarla dolu bir dosya verecek.|
| **Step 2:** Prepare Data | **Adım 2:** Görev |
| 1. project.ino in his file empty lines one that won't show grep type command.<br>2. Then, both the blank lines and // starting with comment lines <br> just press the "clean code" on the screen by eliminating it. | 1. project.ino dosyasındaki boş satırları göstermeyecek bir grep komutu yaz.<br>2. Ardından, hem boş satırları hem de // ile başlayan yorum satırlarını eleyerek sadece "temiz kodu" ekrana bas. |
| **Submit Billi:** 1. Empty line regex'te ^$ (line head and line end adjacent) is performed ifade.For the process of "eliminating" or "not including" something -v let me remind you that you should use (invert-match).<br>2. // characters may require an escape character on some systems, but they are in quotes when searching in plain text "//" it will do its job. | **Altın Bilgi:** 1. Boş satır regex'te ^$ (satır başı ve satır sonu bitişik) ile ifade edilir. Bir şeyi "eleme" veya "dahil etmeme" işlemi için -v (invert-match) kullanman gerektiğini hatırlatayım.<br>2. // karakterleri bazı sistemlerde kaçış karakteri gerektirebilir ama düz metin olarak aratırken tırnak içinde "//" işini görecektir. |
| SOLUTION | CEVAP |
| 1. grep -vE "^$" g3.ino <br><br>> 2. grep -vE "^$|//" g3.ino | 1. grep -vE "^$" g3.ino <br><br> 2. grep -vE "^$|//" g3.ino |
