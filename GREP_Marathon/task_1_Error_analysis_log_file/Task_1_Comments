LEVEL 1/5
## TASK:
Display the lines in system.log that contain the words error or critical, without case sensitivity, together with their line numbers.
## SOLUTION 1
grep -in -e "error" -e "critical" ./system.log && grep -in -e "error" -e "critical" ./system.log | wc -l

## SOLUTION 2
grep -Ei "error|critical" system.log -n

## AMALYST NOTES
-E: "Veya" (|) işaretini kullanabilmek için (Extended Regex).

-i: Büyük/küçük harf duyarsızlığı.

-n: Satır numarası.
