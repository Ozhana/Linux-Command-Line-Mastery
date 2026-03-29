# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO:  | SENARYO: Elimizde bir okulun sinav_sonuclari.txt dosyası var. Dosyada öğrenci adı, matematik notu, fizik notu ve kimya notu bulunuyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Verideki başlık satırını (ilk satırı) atla.<br><br> 2. Her öğrencinin 3 dersinin ortalamasını hesapla ve isminin yanına yazdır. <br><br>3. Eğer ortalaması 85 ve üzerindeyse satırın sonuna "BAŞARILI" ibaresi ekle.<br><br>4. En alt kısımda (END bloğunda) tüm sınıfın genel matematik ortalamasını hesaplayıp yazdır. |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
|  | AWK'ın END bloğu çalışırken, $1 değişkeninin değerini yazdırmayı denersen ne görürsün? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  | AWK'ın END bloğuna ulaştığında $1 (veya $0, $NF gibi tüm alan değişkenleri), dosyanın en son okunan satırındaki değerleri tutmaya devam eder. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
awk '
BEGIN { 
    print "İSİM\tORTALAMA\tDURUM"; 
    print "--------------------------------" 
}
NR > 1 { 
    # 1. Hesaplamalar
    toplam_not = $2 + $3 + $4;
    ortalama = toplam_not / 3;
    
    # 2. Matematik genel toplamı biriktirme (Sütun 2)
    mat_genel_toplam += $2;
    ogrenci_sayisi++;

    # 3. Şartlı Yazdırma
    durum = (ortalama >= 85) ? "BAŞARILI" : "";
    
    # \t tab karakteridir, veriyi hizalar. .2f ise virgülden sonra 2 basamak demektir.
    printf "%s\t%.2f\t\t%s\n", $1, ortalama, durum;
}
END { 
    print "--------------------------------";
    if (ogrenci_sayisi > 0) {
        printf "Sınıf Matematik Ortalaması: %.2f\n", mat_genel_toplam / ogrenci_sayisi;
    }
}' sinav_sonuclari.txt
```
