BEGIN {
    # Başlıkları ve sayaçları hazırla
    printf "%-20s | %-12s | %-10s | %-15s\n", "ZAMAN", "DURUM", "USER", "IP"
    print "----------------------------------------------------------------------"
    accepted = 0; failed = 0;
}

{
    zaman = $1 " " $2 " " $3
    
    # 3. Madde: Yerel ağdan gelenleri (192.168.x.x) direkt atla (next komutu sonraki satıra geçer)
    if ($0 ~ /from 192\.168\./) { next }

    # Sayacımız için genel istatistik
    if ($5 == "Accepted") { accepted++ }
    if ($5 == "Failed" || $5 == "Invalid") { failed++ }

    # 1. & 2. Madde: Kritik Hata ve Root Alarmı
    if ($5 == "Failed" || $5 == "Invalid") {
        
        # Sütunları dinamik bulma: "from" kelimesinden önceki kullanıcıdır, sonraki IP'dir
        # Ama şimdilik senin saydığın sabit sütunlar üzerinden gidelim:
        user = ($5 == "Invalid") ? $9 : $8
        ip = ($5 == "Invalid") ? $11 : $10
        status = ($5 == "Invalid") ? "Invalid User" : "Failed Pwd"

        # Root kontrolü
        alarm = (user == "root") ? "[DIKKAT] " : ""

        # 5. Madde: Port kontrolü (Son sütun $NF)
        if (int($NF) > 50000) {
            printf "%s%-20s | %-12s | %-10s | %-15s (Port: %s)\n", alarm, zaman, status, user, ip, $NF
        }
    }
}

END {
    print "----------------------------------------------------------------------"
    print "SİBER GÜVENLİK ÖZET RAPORU"
    printf "Başarılı Giriş: %d | Başarısız Deneme: %d\n", accepted, failed
    print "Toplam İncelenen Kayıt: " NR
}
