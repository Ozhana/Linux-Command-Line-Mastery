# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 7/10 | ***### Zorluk duzeyi:*** 7/10|
| SCENARIO:  | SENARYO: AWK'ın sadece bir4. metin süzücü değil, aynı zamanda terminalde çalışan bir hesap makinesi olduğunu kanıtlama vakti. Bu görevde bir veri analisti olarak bir öğrenci grubunun sınav sonuçlarını analiz edeceksin. <br><br>Eğitim verdiğin Robotics Club'daki öğrencilerin Python ve Arduino sınav sonuçlarını içeren bir CSV dosyan var. Bu dosya üzerinde karmaşık hesaplamalar (ortalama, geçme/kalma durumu, sınıf birincisi) yapman gerekiyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Ayrıştırıcı Ayarı: Dosya virgülle ayrıldığı için FS (Field Separator) değerini , olarak ayarla (Bunu ister BEGIN içinde yap, ister komut satırında -F, ile).<br><br>2. Genel Ortalama: Her öğrenci için 3 dersin ortalamasını hesapla. Eğer ortalama 50'nin altındaysa satırın başına "KALDI", üstündeyse "GECTI" yazdır.<br><br>3. Başarı Puanı: Ortalama hesaplanırken ağırlıklandırılmış puan kullan: Math %40, Physics %30, Robotics %30 olsun.<br><br>4. Sınıf Ortalaması: Tüm sınıfın genel ortalamasını END bloğunda yazdır. <br><br>5. Varyans Hazırlığı: END bloğunda sadece ortalamayı değil, en yüksek ortalamaya sahip öğrencinin adını ve notunu da yazdır. (Burada bir değişken tutup her satırda if (su_anki > max) kontrolü yapmalısın). |
| Golden Information: | Altin Bilgi: |
|  | AWK'da ^ operatörü üs alma için kullanılır. (x^2) gibi. Eğer standart sapma hesaplamak istersen bu senin çok işine yarayacak. |
| Analytical Question: | Analitik Soru: |
|  | AWK içinde NR (toplam satır sayısı) ve FNR (dosya bazlı satır sayısı) arasındaki fark nedir? Birden fazla dosyayı aynı anda işlerken hangisini kullanmalısın? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  | Geçtiğimiz görevde sorduğum NR ve FNR farkına dair:<br><br>NR (Number of Records): AWK çalışmaya başladığından beri okuduğu toplam satır sayısıdır.<br><br>FNR (File Number of Records): O an okunan mevcut dosyadaki satır sayısıdır.<br><br>Örnek: 10'ar satırlık iki dosyayı işliyorsan; ikinci dosyanın ilk satırında NR 11 olurken, FNR tekrar 1 olur. Bu, birden fazla dosyayı karşılaştırırken (örneğin iki farklı sınıftaki aynı isimli öğrencileri eşleştirirken) hayat kurtarır. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
BEGIN{
FS=",";
printf "%-10s %-10s %-10s %-10s %-10s %-10s\n", "OGRENCI", "MATHS", "PHYSICS", "ROBOTICS", "ORTALAMA", "DURUM";
print "-------------------------------------------------------------";
ortalama = 0;
gecen = 0;
kalan = 0;
sinif_ortalamasi = 0;
mat_top = 0;
phy_top = 0;
rob_top = 0;
en_yuksek_mat = -1;
en_yuksek_phy = -1;
en_yuksek_rob = -1;
en_yuksek_ort = -1;
}
NR>1{
ortalama = $2*0.4 + $3*0.3 + $4*0.3;
mat_top = mat_top + $2;
phy_top = phy_top + $3;
rob_top = rob_top +$4;
durum=(ortalama>=50) ? "GECTI" : "KALDI";
printf "%-10s %-10d %-10d %-10d %-10.2f %-10s\n", $1, $2, $3, $4, ortalama, durum;
(durum=="GECTI") ? gecen++ : kalan++;
if ($2 > en_yuksek_mat){
en_yuksek_mat = $2;
birinci_mat = $1;}

if ($3 > en_yuksek_phy){
en_yuksek_phy = $3;
birinci_phy = $1;}

if ($4 > en_yuksek_rob){
en_yuksek_rob = $4;
birinci_rob = $1;}

if (ortalama > en_yuksek_ort){
en_yuksek_ort = ortalama;
birinci_ogrenci = $1;}

}
END{
sin_ort = (mat_top*0.4 + phy_top*0.3 + rob_top*0.3)/(NR-1);
mat_top = (mat_top)/(NR-1);
phy_top = (phy_top)/(NR-1);
rob_top = (rob_top)/(NR-1);
print "-------------------------------------------------------------";
printf "%-10s %-10d %-10d %-10d %-10.2f\n", "ORTALAMA", mat_top, phy_top, rob_top, sin_ort;
printf "Toplam gecen Ogrenci sayisi = %d\n", gecen;
printf "Toplam kalan ogrenci sayisi = %d\n", kalan;
printf "Tum sinif ortalamasi = %.2f\n", sin_ort;
printf "Matematik Birincisi = %d\n", en_yuksek_mat;
printf "Physics Birincisi = %d\n", en_yuksek_phy;
printf "Robotics Birincisi = %d\n", en_yuksek_rob;
printf "Okul Birincisi = %.2f\n", en_yuksek_ort;
}
```
