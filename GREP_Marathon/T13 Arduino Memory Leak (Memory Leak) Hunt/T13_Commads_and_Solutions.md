# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4/5 | ***### Zorluk duzeyi:*** 4/5|
| SCENARIO: The Arduino code you wrote freezes when it runs for a long time. (The amount of free memory per second from the serial port to monitor memory (RAM) usageFree RAM: XXX bytes) you added a code that prints. If the amount of memory is constantly decreasing, it means there is a leak (leak). | SENARYO: Yazdığın Arduino kodu uzun süre çalıştığında donuyor. Bellek (RAM) kullanımını izlemek için seri porttan her saniye serbest bellek miktarını (Free RAM: XXX bytes) yazdıran bir kod ekledin. Eğer bellek miktarı sürekli azalıyorsa bir sızıntı (leak) var demektir. |
| **Step 1:** Prepare the data (or download from here). This is Python code g13_memory_usage.log it will create the file. | **Adım 1:** Data Olustur (veya buradan indir). Bu Python kodu g13_memory_usage.log dosyasını oluşturacak. |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Memory amount Under 2000 bytes find the first line it fell on. (Hint: grep with 1[0-9]{3} you can use a pattern like). <br><br> 2. Memory amount lowest press the screen for the last 5 situations. (Hint: tail -n 5). <br><br> 3. Challenging Bonus: Just extract the amounts (numbers) of memory and these numbers like a data analyst arithmetic mean compare first and last line to see (roughly). | 1. Bellek miktarının 2000 byte'ın altına düştüğü ilk satırı bul. (İpucu: grep ile 1[0-9]{3} gibi bir desen kullanabilirsin). <br><br> 2. Bellek miktarının en düşük olduğu son 5 durumu ekrana bas. (İpucu: tail -n 5). <br><br> 3. Zorlayıcı Bonus: Sadece bellek miktarlarını (sayıları) ayıkla ve bir veri analisti gibi bu sayıların aritmetik ortalamasını (kabaca) görmek için ilk ve son satırı karşılaştır. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -E "[0-1][0-9]{3}([[:space:]]|$)" g13_memory_usage.log | sort -nr | head -n 1
2. grep -E "[0-1][0-9]{3}([[:space:]]|$)" g13_memory_usage.log | sort -nr | tail -n 1
3. grep -Eo "[0-9][0-9]{3}([[:space:]]|$)" g13_memory_usage.log | sort -n | head -n 1 ; grep -Eo "[0-9][0-9]{3}([[:space:]]|$)" g13_memory_usage.log | sort -n | tail -n 1
```
Real average with GREP and FOR LOOP

``` bash
n=$(grep -Ec "[0-1][0-9]{3}([[:space:]]|$)" g13_memory_usage.log)
t=0
for ((i=1;i<=n;i++));
do
k=$(grep -Eo "[0-9]{4}([[:space:]]|$)" g13_memory_usage.log | sort -n | head -n "$i" | tail -n 1);
((t=t+k));
done
echo "scale=2; $t/$n" | bc
```
