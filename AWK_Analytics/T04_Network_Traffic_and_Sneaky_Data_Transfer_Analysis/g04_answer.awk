{
    # $2 IP adresi, $NF (en sondaki) Byte miktarı
    byte[$2] += $3
    count[$2]++
}

END {
    printf "%-18s | %-15s | %-10s | %-8s\n", "DURUM", "IP ADRESI", "TRAFIK(MB)", "ADET"
    print "----------------------------------------------------------------------"
    
    for (ip in byte) {
        mb = byte[ip] / 1048576
        # 5 MB üzeri alarm (Senin 9 MB mantığını 5'e çektim hocam)
        uyari = (mb >= 5) ? "[YUKSEK TRAFIK]" : "[NORMAL]"
        
        printf "%-18s | %-15s | %-10.2f | %-8d\n", uyari, ip, mb, count[ip] | "sort -nk3"
    }
}
