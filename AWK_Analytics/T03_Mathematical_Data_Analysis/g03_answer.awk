BEGIN{
FS=",";
printf "%-10s %-10s %-10s %-10s %-10s %-10s\n", "OGRENCI", "MATHS", "PHYSICS", "ROBOTICS", "ORTALAMA", "DURUM";
print "-------------------------------------------------------------";
ortalama = 0;
gecen = 0;
kalan = 0;
sinif_ortalamasi = 0;
mat_top = 0;
phy_top = 0;
rob_top = 0;
en_yuksek_mat = -1;
en_yuksek_phy = -1;
en_yuksek_rob = -1;
en_yuksek_ort = -1;
}
NR>1{
ortalama = $2*0.4 + $3*0.3 + $4*0.3;
mat_top = mat_top + $2;
phy_top = phy_top + $3;
rob_top = rob_top +$4;
durum=(ortalama>=50) ? "GECTI" : "KALDI";
printf "%-10s %-10d %-10d %-10d %-10.2f %-10s\n", $1, $2, $3, $4, ortalama, durum;
(durum=="GECTI") ? gecen++ : kalan++;
if ($2 > en_yuksek_mat){
en_yuksek_mat = $2;
birinci_mat = $1;}

if ($3 > en_yuksek_phy){
en_yuksek_phy = $3;
birinci_phy = $1;}

if ($4 > en_yuksek_rob){
en_yuksek_rob = $4;
birinci_rob = $1;}

if (ortalama > en_yuksek_ort){
en_yuksek_ort = ortalama;
birinci_ogrenci = $1;}

}
END{
sin_ort = (mat_top*0.4 + phy_top*0.3 + rob_top*0.3)/(NR-1);
mat_top = (mat_top)/(NR-1);
phy_top = (phy_top)/(NR-1);
rob_top = (rob_top)/(NR-1);
print "-------------------------------------------------------------";
printf "%-10s %-10d %-10d %-10d %-10.2f\n", "ORTALAMA", mat_top, phy_top, rob_top, sin_ort;
printf "Toplam gecen Ogrenci sayisi = %d\n", gecen;
printf "Toplam kalan ogrenci sayisi = %d\n", kalan;
printf "Tum sinif ortalamasi = %.2f\n", sin_ort;
printf "Matematik Birincisi = %d\n", en_yuksek_mat;
printf "Physics Birincisi = %d\n", en_yuksek_phy;
printf "Robotics Birincisi = %d\n", en_yuksek_rob;
printf "Okul Birincisi = %.2f\n", en_yuksek_ort;
}
