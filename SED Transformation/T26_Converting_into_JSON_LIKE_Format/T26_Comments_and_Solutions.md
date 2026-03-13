# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 8.5/10 | ***### Zorluk duzeyi:*** 8.5/10|
| SCENARIO:  | SENARYO: Bir veri analisti olarak size bir siber güvenlik cihazından "pipe separated" ( | ile ayrılmış) ham veriler geliyor. Ancak analiz aracınız bu veriyi sadece anahtar-değer (key-value) çifti şeklinde kabul ediyor. Sizin bu düz metni, awk kullanmadan sadece sed ile yapılandırılmış bir formata sokmanız gerekiyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| Golden Information: | Altin Bilgi: |
|  | Regex'te parantez içinde parantez açarak verinin hem tamamını hem de bir parçasını aynı anda yakalayabilirsiniz. <br><br> Örn: (([0-9]{2})\/([0-9]{2})) <br> Burada \1 tüm tarihi (gün/ay) verirken, \2 sadece günü, \3 sadece ayı verir. Bu, JSON gibi yapılandırılmış veri oluştururken size muazzam bir esneklik sağlar. |
| Analytical Question: | Analitik Soru: |
|  | JSON gibi hiyerarşik bir format oluştururken, sed'in satır bazlı (line-by-line) çalışma prensibi bize ne gibi bir kısıtlama getirir? Örneğin birden fazla satıra yayılmış bir JSON objesini sed ile yönetmek neden "normal" bir substitution (s///) işleminden çok daha zordur? |
|  | sed'in satır bazlı olması, JSON gibi blok (multiline) yapılarda bizi zorlar. Çünkü sed bir satırı bitirip diğerine geçtiğinde eski satırı unutur. Eğer bir JSON objesi 5 satıra yayılmışsa, sed'in "Hold Space" (yedek bellek) özelliğini kullanmak gerekir ki bu da komutları çok karmaşıklaştırır. Bu yüzden sed genellikle tek satırlık (inline) JSON'lar için tercih edilir |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|  | 1. Dinamik Etiketleme: Her satırı şu formata çevirin: {"timestamp": "TARİH", "user": "KULLANICI", "event": "OLAY", "risk_score": "SKOR"}. <br><br> 2. Skor Normalizasyonu: Risk skorları 0-100 arasında geliyor. Sizden istenen, 9[0-9] (90-99 arası) olan tüm skorların sonuna _CRITICAL ibaresini, sed'in geri çağırma (\n) özelliği ile eklemeniz. <br><br> 3. Gereksiz Veri Budama: Satır sonundaki teknik hata kodlarını (Örn: ERR_CODE: 404) tamamen silin, JSON formatına dahil etmeyin. <br><br> 4. Tarih Maskeleme: Analiz raporunda gün ve ay görünmeli ama yıl kısmı güvenlik gereği XXXX olarak değiştirilmeli (Örn: 12/03/2026 -> 12/03/XXXX). <br><br> 5. Otomasyon: Bu karmaşık dönüşümü tek bir sed komut zinciri ile yapın. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E 's#^([0-9]{2}/[0-9]{2})/[0-9]{4}[[:space:]]\|[[:space:]]([^[:space:]]+)[[:space:]]\|[[:space:]]([^[:space:]]+)[[:space:]]\|[[:space:]]([0-9]+)[[:space:]]\|[[:space:]]ERR_CODE:[[:space:]]([0-9]{3})$#{"timestamp": "\1/XXXX", "user": "\2", "event": "\3", "risk_score": "\4", "err_code": "\5"}#' g26_raw_traffic.log
```
