# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: Entry-exit logs of the laboratory door g19_access_logs.txt it is kept in his file. Format: <br><br> GÜN-AY-YIL SAAT:DAKİKA:SANİYE \| KULLANICI_ID \| İŞLEM \| KAPI_DURUMU <br><br> Example: 10-03-2026 14:20:15 \| USER_45 \| ENTRY \| SUCCESS | SENARYO: Laboratuvar kapısının giriş-çıkış logları g19_access_logs.txt dosyasında tutuluyor. Format: <br><br> GÜN-AY-YIL SAAT:DAKİKA:SANİYE \| KULLANICI_ID \| İŞLEM \| KAPI_DURUMU <br><br> Örnek: 10-03-2026 14:20:15 \| USER_45 \| ENTRY \| SUCCES |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only afternoon (hour 12:00:00 with 17:59:59 find transactions taking place between). <br> Hint: Focus on the beginning of the clock part: 1[2-7]: <br><br> 2. Between these hours faulty find login attempts (Process ENTRY it will happen, but Door Status FAIL will be). <br><br> 3. Challenging Part: Which user (USER_XX) find out how many times you received "FAIL" and sort from most to least error. <br><br> 4. Final Touch (Bash): Can you print the ID of the first 3 users who made the most mistakes on the screen as "SUSPECT LIST: ID1, ID2, ID3" (in a single line)? (Hint: head -n 3 and the paste -sd "," or you can use loop). | 1. Sadece öğleden sonra (saat 12:00:00 ile 17:59:59 arası) gerçekleşen işlemleri bul. <br> İpucu: Saat kısmının başlangıcına odaklan: 1[2-7]: <br><br> 2. Bu saatler arasındaki hatalı giriş denemelerini bul (İşlem ENTRY olacak ama Kapı Durumu FAIL olacak). <br><br> 3. Zorlayıcı Kısım: Hangi kullanıcının (USER_XX) kaç kez "FAIL" aldığını bul ve en çok hata yapandan en aza doğru sırala. <br><br> 4. Final Dokunuşu (Bash): En çok hata yapan ilk 3 kullanıcının ID'sini ekrana "ŞÜPHELİ LİSTESİ: ID1, ID2, ID3" şeklinde (tek satırda) yazdırabilir misin? (İpucu: head -n 3 ve paste -sd "," veya döngü kullanabilirsin).|
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. grep -E "^[^ ]+ 1[2-7]:([0-9]){2}:([0-9]){2}" g19_access_logs.txt

2. grep -E "^[^ ]+ 1[2-7]:([0-9]){2}:([0-9]){2}" g19_access_logs.txt | grep "ENTRY" | grep "FAIL"

3A. grep -E "^[^ ]+ 1[2-7]:([0-9]){2}:([0-9]){2}" g19_access_logs.txt | grep "ENTRY" | grep "FAIL" | grep -oE "USER_[0-9]{1,2}" | sort |uniq -c | sort -nr

-- bu kodda cut - kullanmak istememistim ama cut -d hali de asagida

3B. grep -E "^[^ ]+ 1[2-7]:([0-9]){2}:([0-9]){2}" g19_access_logs.txt | grep "ENTRY" | grep "FAIL" | cut -d' ' -f4 | sort |uniq -c | sort -nr

4. for ((i=1;i<=top;i++))
do
n=$(grep -E "^[^ ]+ 1[2-9]:([0-9]){2}:([0-9]){2}" g19_access_logs.txt | grep "ENTRY" | grep "FAIL" | cut -d' ' -f4 | sort |uniq -c | sort -nr | head -n "$i" | tail -n 1)
echo -n "$n "
done
```
