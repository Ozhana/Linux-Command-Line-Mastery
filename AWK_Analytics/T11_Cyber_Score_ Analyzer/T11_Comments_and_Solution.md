# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 8/10 | ***### Zorluk duzeyi:*** 8/10|
| SCENARIO: You're monitoring the school's network security. He has the number of "suspicious transactions" made by each student or staff member. Take these numbers from you risk score calculator and this score to a textual level I want you to set up a system that translates. | SENARYO: Okulun ağ güvenliğini denetliyorsun. Elinde her bir öğrencinin veya personelin yaptığı "şüpheli işlem" sayıları var. Senden, bu sayıları alıp risk puanı hesaplayan ve bu puanı metinsel bir seviyeye çeviren bir sistem kurmanı istiyorum. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Risk Calculation Function: To the very beginning of the script function risk_skoru(g, s, e) write a function named.<br><br>Formula:<br><br>$$Risk = (g \times 1) + (s \times 2) + (e \times 5)<br><br>2. Level Determination Function: function seviye_bul(skor) write a second function named.<br>If score < 5: "LOW"<br>5 <= If score < 15: "MEDIUM"<br>If score >= 15: "HIGH"<br><br>3. Application: Pass each line in the main block through these functions and report the result.<br><br>4. Mathematician Touch: END calculate the overall "Average Risk Score" of the system in your block. | 1. Risk Hesaplama Fonksiyonu: Scriptinin en başına function risk_skoru(g, s, e) adında bir fonksiyon yaz.<br><br>Formül:<br><br>$$Risk = (g \times 1) + (s \times 2) + (e \times 5)2. $$Seviye Belirleme Fonksiyonu: function seviye_bul(skor) adında ikinci bir fonksiyon yaz.<br>Skor < 5 ise: "DÜŞÜK"<br>5 <= Skor < 15 ise: "ORTA"<br>Skor >= 15 ise: "YÜKSEK"<br><br>3. Uygulama: Ana blokta her satırı bu fonksiyonlardan geçir ve sonucu raporla.<br><br>4. Matematikçi Dokunuşu: END bloğunda sistemin genel "Ortalama Risk Skoru"nu hesapla. |
| Golden Information: | Altin Bilgi: |
| Why Do We Write Our Own Function?<br><br>If you need to perform an operation (e.g. complex percentage calculation, date formatting, or cybersecurity scoring) more than once within the script, you can trap it within a function and call it from anywhere you want.<br><br>Function Structure:<br><br> function puanla(puan) {<br>    if (puan > 90) return "A"<br>    else if (puan > 80) return "B"<br>    else return "C"<br>}|  |
| Analytical Question: | Analitik Soru: |
|  |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
function risk_skoru(g, s, e){
	return g + (s*2) + (e*5)
	}
function seviye_bul(skor) {
	if (skor < 5)
		{return "DUSUK"}
	else if ( skor < 15)
		{return "ORTA"}
	else
		{return "YUKSEK"}
		}

BEGIN {FS=",";
	istek_kisi = toupper(kisi);
	genel_toplam = 0;
	hatali_sorgu_toplam = 0;
	basarisiz_giris_toplam = 0;
	yetkisiz_erisimtoplam = 0;
	skorlar = 0;
	printf "%-15s | %-15s | %-15s | %-15s | %-15s | %-15s |\n", "Kullanici", "Basarisiz_Giris", "Hatali_Sorgu", "Yetkisiz_Erisim", "Skor", "Durum";
	print "---------------------------------------------------------------------------------------------------";
}
{

hatali_sorgu_toplam+=$3;
basarisiz_giris_toplam+=$2;
yetkisiz_erisimtoplam+=$4;
current_kisi = toupper($1);
skor = risk_skoru($2, $3, $4);
skorlar += skor;
durum = seviye_bul(skor);
if (istek_kisi == "" || current_kisi == istek_kisi){
	genel_toplam++;
	printf "%-15s | %-15d | %-15d | %-15d | %-15s | %-15s |\n", current_kisi, $2, $3, $4, skor, durum;
	}
}
END {
print "----------------------------------------------------------------------------------------------------";
if (genel_toplam > 0) {
hatali_sorgu_ortalama = hatali_sorgu_toplam / genel_toplam;
basarisiz_giris_ortalama = basarisiz_giris_toplam / genel_toplam;
yetkisiz_giris_ortalama = yetkisiz_erisimtoplam / genel_toplam;
skor_ortalama = skorlar / genel_toplam;
	printf "%-15s | %-15s | %-15s | %-15s | %-15s |\n", "ORTALAMALAR", basarisiz_giris_ortalama, hatali_sorgu_ortalama, yetkisiz_giris_ortalama, skor_ortalama;
	}
else print "Aranan Kisi Listede yok...!!!";
}
```
