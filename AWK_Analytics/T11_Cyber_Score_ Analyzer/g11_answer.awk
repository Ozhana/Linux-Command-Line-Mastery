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
