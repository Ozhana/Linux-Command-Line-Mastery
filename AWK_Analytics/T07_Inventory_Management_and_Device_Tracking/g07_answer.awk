awk '
BEGIN { 
    RS = "END_RECORD\n"; 
    FS = "\n"; 
    printf "%-10s | %-20s\n", "ID", "CIHAZ ADI";
    print "-----------------------------------";
    fed_count = 0 
}
{
    # Filtreleme: 3. satır Fedora içeriyor mu VE 4. satır Aktif mi?
    if ($3 ~ /Fedora/ && $4 ~ /Aktif/) {
        fed_count++;
        split($1, id_arr, ": ");
        split($2, cihaz_arr, ": ");
        printf "%-10s | %-20s\n", id_arr[2], cihaz_arr[2];
    }
}
END { 
    print "-----------------------------------";
    print "Toplam Aktif Fedora Cihazı: " fed_count 
}' g07_inventory.txt
