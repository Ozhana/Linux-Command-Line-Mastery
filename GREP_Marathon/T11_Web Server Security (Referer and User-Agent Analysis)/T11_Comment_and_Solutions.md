# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4/5 | ***### Zorluk duzeyi:*** 4/5|
| SCENARIO: You analyze traffic to a website. Some bots use strange “User-Agent” (browser info) to disguise themselves, or send no “Referer” (where it came from) information at all. Your job is to catch suspicious bot traffic. | SENARYO: Bir web sitesine gelen trafikleri analiz ediyorsun. Bazı botlar, kendilerini gizlemek için garip "User-Agent" (tarayıcı bilgisi) kullanırlar veya hiç "Referer" (nereden geldiği) bilgisi göndermezler. Senin görevin, şüpheli bot trafiğini yakalamak. |
| **Step 1:** Prepare the data (or download from here). This is Python code g11_web_access.log it will create the file. Format: IP [Zaman] "Method URL" Statu "Referer" "User-Agent" | **Adım 1:** Data Olustur (veya buradan indir). Bu Python kodu g11_web_access.log dosyasını oluşturacak. Format: IP [Zaman] "Method URL" Statu "Referer" "User-Agent" |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Those whose referer information is empty ("-") find. <br> Hint: Only - if you search, you will hit hyphens everywhere. "-" (including nails) or " - " you should search as follows. <br><br> 2. Through these lines just "Python" or "Curl" starting with (i.e. not real person, bot/script) User-Agentfilter 's. <br><br> 3. Bonus: List which IPs these bots came from and find out the total number. | 1. Referer bilgisi boş olanları ("-") bul. <br> İpucu: Sadece - aratırsan her yerdeki tirelere çarparsın. "-" (tırnaklar dahil) veya " - " şeklinde aratmalısın. <br><br> 2. Bu satırların içinden sadece "Python" veya "Curl" ile başlayan (yani gerçek insan değil, bot/script) User-Agent'ları süz. <br><br> 3. Bonus: Bu botların hangi IP'lerden geldiğini listele ve toplam sayısını bul. |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |
### Web Log Analizi Komutları

Aşağıdaki komutlar, erişim logları içerisindeki Python ve Curl isteklerini filtreleyerek IP adreslerine göre sıralar:

```bash
grep -E "\"-\"|\" - \"" g11_web_access.log | grep -iE "python|curl" | grep -E "^([0-9]{1,3}.){3}[0-9]{1,3}" | cut -d' ' -f1 |sort |uniq -c | sort -nr

OR

grep -E "\"-\"|\" - \"" g11_web_access.log | grep -iE "python|curl" | cut -d' ' -f1 |sort |uniq -c | sort -nr
