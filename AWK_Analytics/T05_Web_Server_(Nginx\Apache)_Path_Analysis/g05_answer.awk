BEGIN {
    failed = 0;
    success = 0;
    printf "%-25s | %-10s\n", "TEMIZ PATH", "HIT ADEDI";
    print "----------------------------------------------------"
}

{
    # URL'yi parçala (? işaretinden öncesini al)
    split($4, parca, "?")
    path = parca[1]
    
    # Hit sayısını artır
    hit[path]++

    # Durum kodlarını kontrol et ($NF her zaman sondur)
    if ($NF == "404" || $NF == "500") {
        failed++
    } else if ($NF == "200") {
        success++
    }
}

END {
    # Sıralama için bu bloğun çıktısını dışarıda pipe yapacağız
    for (p in hit) {
        printf "%-25s | %-10d\n", p, hit[p]
    }
    
    # Özet bilgileri stderr'e veya ayrı bir print ile basabiliriz
    # Tasarımın bozulmaması için bunları sıralamaya sokmamak en iyisi
    print "----------------------------------------------------"
    printf "BASARILI (200) : %d\n", success
    printf "HATALI (404/500): %d\n", failed
}
