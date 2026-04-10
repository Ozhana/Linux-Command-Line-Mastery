# g06_answer.awk
# Karisik verilen zamani saniyeye cevir
# sonra da satirin basina ekle
# 6. Gorevde zaman satirin basinda degilse ilgili yere eklenebilir ?

function to_second(p){
split (p,  a, ":");
return a[1]*3600 + a[2]*60 +a[3];
}
BEGIN {
}
{
print to_second($1), $0
}
END {
}
