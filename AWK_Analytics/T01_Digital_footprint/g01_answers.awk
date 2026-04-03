BEGIN { 
    # 5. Madde: Başlık
    printf "%-10s | %-15s | %-10s | %-10s\n", "USER_ID", "ACTION", "AMOUNT", "DEVICE"
    print "------------------------------------------------------------"
    toplam = 0
    uzun_islem = 0
}

{
    # 1. Madde: Sadece PROJECT_COMPLETE olanlar
    if ($2 == "PROJECT_COMPLETE") {
        
        # 4. Madde: Cihaz Fedora_v43 ise ilk 3 karakteri al (substr)
        cihaz = $5
        if (cihaz == "Fedora_v43") {
            cihaz = substr(cihaz, 1, 3)
        }

        # Çıktıyı hizalı yazdıralım
        printf "%-10s | %-15s | %-10.2f | %-10s\n", $1, $2, $3, cihaz
        
        # 3. Madde: Toplam kazancı hesapla
        toplam += $3
    }

    # 2. Madde: 60 dakikadan fazla sürenleri say (4. sütun "90min" formatında olduğu için int() ile temizle)
    if (int($4) > 60) {
        uzun_islem++
    }
}

END {
    print "------------------------------------------------------------"
    print "FREELANCE FINANSAL RAPORU"
    printf "Toplam Kazanç: %.2f USD\n", toplam
    print "60 Dakikayı Geçen İşlem Sayısı: " uzun_islem
    print "TOPLAM ISLEM (Satır Sayısı): " NR
}
