# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: Elinde iki dosya var.<br><br>ogrenciler.txt: (ID ve İsim içeriyor) <br>notlar.txt: (ID ve Sınav Notu içeriyor)<br><br>Senden, bu iki dosyayı "ID" üzerinden birleştirip (Join), ismi ve notu yan yana getirmeni isteyeceğim. Ama dikkat! Bazı öğrencilerin notu olmayabilir, onları da "Girilmedi" olarak işaretlemelisin. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Separator Setting: Because the files are separated by commas FS="," you should use it<br><br>2. Memory the First File: NR == FNR provided that ogrenciler.txt read the file and make the ID the key to name (in an arrayisimler[ID] = Isim) store.<br><br>3. Compare Second File: NR > FNR (or just the inverse of the first condition) case notlar.txt read file. Pull the name corresponding to the ID from the array.<br><br>4. Missing Data Check: If an ID is in the first file but there is no note in the second file END report that student as "Not Took the Exam" on your blog or by some logic.<br><br>5. Clean Report: Let the output be in the following format:
ID \| ISIM \| NOT \| DURUM | 1. Ayırıcı Ayarı: Dosyalar virgülle ayrıldığı için FS="," kullanmalısın.<br><br>2. Birinci Dosyayı Hafızaya Al: NR == FNR koşuluyla ogrenciler.txt dosyasını oku ve ID'yi anahtar yaparak isimleri bir dizide (isimler[ID] = Isim) sakla.<br><br>3. İkinci Dosyayı Karşılaştır: NR > FNR (veya sadece ilk koşulun tersi) durumunda notlar.txt dosyasını oku. ID'ye karşılık gelen ismi diziden çek.<br><br>4. Eksik Veri Kontrolü: Eğer bir ID birinci dosyada var ama ikinci dosyada notu yoksa, END bloğunda veya bir mantıkla o öğrenciyi "Sınava Girmedi" olarak raporla.<br><br>5. Temiz Rapor: Çıktı şu formatta olsun:
ID \| ISIM \| NOT \| DURUM \|
| Golden Information: | Altin Bilgi: |
| FNR vs NR: Two-File Analysis Logic<br><br>NR (Number of Records): total number of lines read since AWK started working.<br><br>FNR (File Number of Records): Read at that moment in the active file number of rows.<br><br>Magic Formula: NR == FNR
If NR == FNR ise, AWK first file he's reading. If NR > FNR if so, the first file is finished and to the second file passed. | FNR vs NR: İki Dosyalı Analiz Mantığı<br><br>NR (Number of Records): AWK çalışmaya başladığından beri okunan toplam satır sayısı.<br><br>FNR (File Number of Records): O an okunan aktif dosyadaki satır sayısı.<br><br>Sihirli Formül: NR == FNR
Eğer NR == FNR ise, AWK birinci dosyayı okuyordur. Eğer NR > FNR ise, birinci dosya bitmiş ve ikinci dosyaya geçilmiştir. |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN {
	FS=",";
	printf "%-15s | %-15s | %-15s | %-10s\n", "OGRENCI_ID", "OGRENCI_ISIM", "OGRENCI_PUAN", "DURUM";
	print "---------------------------------------------------------------";
}

NR == FNR {
	isimler[$1] = $2;
	next;
}

{
	if ($1 in isimler){
		printf "%-15d | %-15s | %-15d | %-10s\n", $1, isimler[$1], $2, "GIRDI";
		delete isimler[$1];
	}
}

END {
	for (num in isimler){
		printf "%-15d | %-15s | %-15s | %-10s\n", num, isimler[num], "-", "GIRMEDI";
	}
	print "---------------------------------------------------------------";
}
```
