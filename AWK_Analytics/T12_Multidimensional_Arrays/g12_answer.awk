BEGIN { 
    FS = ","
    # Günlerin sırasını manuel belirleyelim ki karışık basmasın
    sirali_gunler = "PAZARTESI,SALI,CARSAMBA,PERSEMBE,CUMA"
    split(sirali_gunler, gun_listesi, ",")
}

{
    # 1. Veri Temizliği (Header'ı atla ve anomalileri ele)
    if (NR == 1 || $3 < 0 || $3 > 1000) next;

    dep = toupper($1)
    gun = toupper($2)
    
    # 2. Çok Boyutlu Diziye Ekleme
    # AWK arkada bunu "MATH\034PAZARTESI" gibi bir anahtar yapar
    matris[dep, gun] += $3
    
    # Departmanları kayıt altında tut
    dep_listesi[dep] = 1
}

END {
    # --- BAŞLIKLARI BAS (Günler) ---
    printf "%-10s", "DEP/GUN"
    for (i=1; i<=5; i++) printf " | %-10s", gun_listesi[i]
    printf " | %-10s\n", "TOPLAM"
    print "-------------------------------------------------------------------------------"

    # --- SATIRLARI BAS (Departmanlar) ---
    for (d in dep_listesi) {
        # Wrap/Truncate Denemesi: 5 karakterden uzunsa kes
        dep_gorunum = (length(d) > 5) ? substr(d, 1, 5) "." : d
        printf "%-10s", dep_gorunum
        
        satir_toplam = 0
        for (i=1; i<=5; i++) {
            g = gun_listesi[i]
            deger = matris[d, g] # Eğer o gün harcama yoksa AWK 0 kabul eder
            printf " | %-10.2f", deger
            satir_toplam += deger
            sutun_toplam[g] += deger # Sütun toplamı için biriktir
        }
        printf " | %-10.2f\n", satir_toplam
        genel_toplam += satir_toplam
    }

    # --- ALT TOPLAMLARI BAS (Genel) ---
    print "-------------------------------------------------------------------------------"
    printf "%-10s", "GENEL"
    for (i=1; i<=5; i++) {
        g = gun_listesi[i]
        printf " | %-10.2f", sutun_toplam[g]
    }
    printf " | %-10.2f\n", genel_toplam
}
