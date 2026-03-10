# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: You wrote a PID controller for your line-tracking robot. How far the robot deviates from the line (Error) you are logging If error (Error) if it gets too high in a row, it means the robot is off the track. | SENARYO: Çizgi izleyen robotun için bir PID kontrolcü yazdın. Robotun çizgiden ne kadar saptığını (Error) logluyorsun. Eğer hata (Error) üst üste çok yüksek gelirse robot pistten çıkıyor demektir. |
| **Step 1:** Prepare the data (or download from here). This is Python code g14_pid_debug.log it will create the file. Format: Time,Target,Current,Error | **Adım 1:** Data Olustur (veya buradan indir). Bu Python kodu g14_pid_debug.log dosyasını oluşturacak. Format: Time,Target,Current,Error |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Error (Error) is greater than 50 find all lines. (Hint: Error in column 4, at the end of the line). <br><br>2. These are faulty situations the first moment he started (first line) and the last moment it ended show (last line) with a single chain of commands or consecutive commands. <br><br> 3. Mathematical Challenge: When the robot leaves the track (Error > 50) average error try to calculate (whether with your cycle or what you just learned awk with). | 1. Hatanın (Error) 50'den büyük olduğu tüm satırları bul. (İpucu: Error 4. sütunda, satır sonunda). <br><br> 2. Bu hatalı durumların başladığı ilk anı (ilk satırı) ve bittiği son anı (son satırı) tek bir komut zinciriyle veya ardışık komutlarla göster. <br><br> 3. Matematiksel Meydan Okuma: Robotun pistten çıktığı andaki (Error > 50) ortalama hatayı hesaplamaya çalış (ister senin döngünle, ister yeni öğrendiğin awk ile). |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -E "[5-9][0-9]{1,2}($)" g14_pid_debug.log
2. grep -E "[5-9][0-9]{1,2}($)" g14_pid_debug.log | sort -t, -k4r

n=$(grep -Ec "[5-9][0-9]{1,2}($)" g14_pid_debug.log)
for ((i=1; i<=n; i++)); do k=$(grep -Eo "[5-9][0-9]{1,2}($)" g14_pid_debug.log | sort -n | head -n "$i" | tail -n 1); ((t=t+k));  done
echo "scale=2; $t / $n" |bc
```
