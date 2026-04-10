BEGIN {
	FS=",";
	printf "%-15s | %-15s | %-15s | %-10s\n", "OGRENCI_ID", "OGRENCI_ISIM", "OGRENCI_PUAN", "DURUM";
	print "---------------------------------------------------------------";
}

NR == FNR {
	isimler[$1] = $2;
	next;
}

{
	if ($1 in isimler){
		printf "%-15d | %-15s | %-15d | %-10s\n", $1, isimler[$1], $2, "GIRDI";
		delete isimler[$1];
	}
}

END {
	for (num in isimler){
		printf "%-15d | %-15s | %-15s | %-10s\n", num, isimler[num], "-", "GIRMEDI";
	}
	print "---------------------------------------------------------------";
}
