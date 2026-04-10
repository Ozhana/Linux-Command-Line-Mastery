BEGIN { 
    FS=":";
    # Dışarıdan gelen 'dep' değişkenini bir kez büyük harfe çevirip sabitleyelim
    # Böylece her satırda toupper(dep) demek zorunda kalmayız.
    dep = toupper(dep); 
    
    printf "%-10s | %-12s | %-15s | %-20s |\n", "Full Name", "Login Count", "Last IP", "Status";
    print "-------------------------------------------------------------------------";
}

NR == FNR {
    # Dosyadaki departmanı da (Math, math, MATH) büyük harfe çevirip kıyaslıyoruz
    current_dept = toupper($3);

    if (dep == "" || current_dept == dep) {
        full_name[$1] = $2;
        department[$1] = current_dept; # Artık hafızada hepsi büyük harf (IT, MATH, HR)
    }
    next;
}

{
    # İkinci dosya: logins.txt
    if ($1 in full_name) {
        # Mantık: IT değilse VE login > 10 ise ŞÜPHELİ
        if (department[$1] != "IT" && $2 > 10) {
            durum = "ŞÜPHELİ YOĞUNLUK";
        } else {
            durum = "GÜVENLİ";
        }
        
        printf "%-10s | %-12d | %-15s | %-20s |\n", full_name[$1], $2, $3, durum;
        delete full_name[$1]; # İşlendi, sil.
    }
}

END {
    # Geriye kalanlar login olmayan (Pasif) kullanıcılardır
    for (usr in full_name) {
        printf "%-10s | %-12s | %-15s | %-20s |\n", full_name[usr], "0", "N/A", "PASIF KULLANICI";
    }
    print "-------------------------------------------------------------------------";
}
