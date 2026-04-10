# g06_answer_part_2.awk
BEGIN {
printf "%-28s | %-10s | %-13s -> %-12s | %-10s \n", "SANIYE" , "ZAMAN", "KULLANICI", "IP", "ATAK SAY.";
print "---------------------------------------------------------------"
toplam_saldiri = 0;
}
{saldiri_sayisi[$1]++;
toplam_saldiri++;
hedef[$1] = $7 " -> " $9;
ips[$9]++;


}
END {
for (k in hedef) {
    status = (saldiri_sayisi[k] >=3) ? "KRITIK: Brute-Force Tespiti!" : "";
    printf "%-28s | %-10d | %-10s | %-25s | %-10d \n", status, $1, $2, hedef[k], saldiri_sayisi[k];
	}
print "---------------------------------------------------"
print "toplam saldiri sayisi = ", toplam_saldiri;
unique_ip_sayisi = 0;
for (i in ips) { 
unique_ip_sayisi++ 
print i, ips[i]}

}
