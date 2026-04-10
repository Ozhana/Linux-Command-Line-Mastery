BEGIN { 
    RS = "END_RECORD\n"; 
    FS = "\n"; 
    printf "%-10s | %-20s\n", "ID", "CIHAZ ADI";
    print "-----------------------------------";
    found_count = 0 
}
{
    # Hem logdaki veriyi hem de dışarıdan gelen değişkeni küçük harfe çekip kıyaslıyoruz
    # Böylece kullanıcı 'fedora', 'Fedora' veya 'FEDORA' yazsa da çalışır.
    if (tolower($3) ~ tolower(os_tipi) && tolower($4) ~ tolower(durumu)) {
        found_count++;
        split($1, id_arr, ": ");
        split($2, cihaz_arr, ": ");
        
        # Sadece değerleri ekrana basarken küçültüyoruz (veya olduğu gibi bırakabilirsin)
        printf "%-10s | %-20s\n", id_arr[2], tolower(cihaz_arr[2]);
    }
}
END { 
    print "-----------------------------------";
    if (found_count == 0) {
        print "Aranan kriterlerde cihaz bulunamadı!"
    } else {
        # Artık sadece Fedora değil, aranan neyse onun sayısını veriyoruz
        print "Eşleşen Toplam Cihaz Sayısı: " found_count 
    }
}
