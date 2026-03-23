# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: You have a network traffic log in your hand (g33_network.log). Sometimes an “Attack Attempt” ( on the systemATTEMPT) is being made, and immediately afterwards (in the next line) the "Result" of this initiative (RESULT) writes. It's just your duty "Faulty Attempts" (i.e., binaries from FAILURE immediately after ATTEMPT) reporting in one line. | SENARYO: Elinizde bir ağ trafik logu var (g33_network.log). Bazen sisteme bir "Saldırı Girişimi" (ATTEMPT) yapılıyor ve hemen ardından (bir sonraki satırda) bu girişimin "Sonucu" (RESULT) yazıyor. Sizin göreviniz, sadece "Hatalı Girişimleri" (yani ATTEMPT'ten hemen sonra FAILURE gelen ikilileri) tek bir satırda raporlamak. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| Open Window (N): 1. N pull the next line next to the current line using the command. You now have two lines in "Pattern Space" (between them \n with character). <br><br>2. Catch Duos: If inside the window ATTEMPT and the FAILURE words one under the other (in between \n if it exists); <br><br>3. Format: This duo [ALERT] Attempted by USER -> Outcome: FAILURE format it and print it.<br><br>4. Slide Window (D): After the process is finished, delete the first line of the window and move on to the next D research and use the command. <br><br>5. Filter: If binary SUCCESS if it ends with, don't print anything. | 1. Pencereyi Aç (N): N komutunu kullanarak mevcut satırın yanına bir sonraki satırı çekin. Artık "Pattern Space" içinde iki satırınız var (aralarında \n karakteriyle). <br><br>2. İkilileri Yakala: Eğer pencerenin içinde ATTEMPT ve FAILURE kelimeleri alt alta (arada \n varken) geçiyorsa; <br><br>3. Formatla: Bu ikiliyi [ALERT] Attempted by USER -> Outcome: FAILURE formatına getirip yazdırın. <br><br>4. Pencereyi Kaydır (D): İşlem bittikten sonra pencerenin ilk satırını silip bir sonrakine geçmek için D komutunu araştırın ve kullanın. <br><br>5. Filtre: Eğer ikili SUCCESS ile bitiyorsa, hiçbir şey yazdırmayın. |
| Golden Information: | Altin Bilgi: |
| This trio, sed creates a “window” (window) inside: <br><br>N (Next): Adds the next line to the current field. (Makes the window larger: line 1 + \n + line 2).<br><br>P (Print): Just inside the window first line (first \nPresses part up to. <br><br>D (Delete): Just inside the window first line deletes and rewinds the loop (without reading a new line). <br><br>Why d instead D we use? <br><br>Sir, d (little d) deletes the entire window and reads a new line. D (capital D) deletes only the top one, makes the bottom one the "new top line" and continues the loop. In this way, you progress by "sliding" without missing any lines. | Bu üçlü, sed içinde bir "pencere" (window) oluşturur: <br><br>N (Next): Bir sonraki satırı mevcut alana ekler. (Pencereyi büyütür: 1. satır + \n + 2. satır). <br><br>P (Print): Sadece pencerenin içindeki ilk satırı (ilk \n'e kadar olan kısmı) basar.<br><br> D (Delete): Sadece pencerenin içindeki ilk satırı siler ve döngüyü başa sarar (yeni satır okumadan).<br><br>Neden d yerine D kullanıyoruz? <br><br>Hocam, d (küçük d) tüm pencereyi siler ve yeni bir satır okur. D (büyük D) ise sadece en üsttekini siler, alttakini "yeni üst satır" yapar ve döngüye devam eder. Bu sayede hiçbir satırı kaçırmadan "kayarak" ilerlersiniz. |
| Analytical Question: | Analitik Soru: |
| Sometimes in the log file ATTEMPT after line RESULT it doesn't come, it doesn't come together SYSTEM: Periodic Check enters. What you wrote N how does the command behave in this case? To the window ATTEMPT and the SYSTEM when you get your lines, the next one RESULT what strategy should you follow to catch the line? | Log dosyasında bazen ATTEMPT satırından sonra RESULT gelmiyor, araya SYSTEM: Periodic Check giriyor. Sizin yazdığınız N komutu bu durumda nasıl davranır? Pencereye ATTEMPT ve SYSTEM satırlarını aldığında, bir sonraki RESULT satırını yakalamak için nasıl bir strateji izlemelisiniz? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
| Sometimes in the log file ATTEMPT after line RESULT it doesn't come, it doesn't come together SYSTEM: Periodic Check enters. What you wrote N how does the command behave in this case? To the window ATTEMPT and the SYSTEM when you get your lines, the next one RESULT what strategy should you follow to catch the line? | Sizin ilk çözümünüzdeki pipe yapısında, eğer ilk sed bir satırı birleştirip dışarı atarsa, ikinci sed o satırı artık "iki ayrı satır" olarak değil "tek bir uzun satır" olarak görür. Bu durum, karmaşık loglarda bazen regex'in satır başı (^) işaretlerini şaşırmasına neden olabilir. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E '
    :start
    /ATTEMPT:/ {
        N;                   # Bir sonraki satırı (RESULT veya SYSTEM) içeri al
        /[[:space:]]RESULT:/ {    # Eğer ikinci satır RESULT ise
            s/\n/ /;         # Birleştir
            /FAILURE/I p;    # Sadece Failure ise yazdır
            d;               # Temizle ve yeni satıra geç
        }
        /[[:space:]]SYSTEM:/ {    # Eğer araya SYSTEM girdiyse
            s/\n/ /;         # Onu da birleştir
            b start;         # Başa dön (tekrar N ile RESULT aramaya devam et)
        }
    }
    d;                       # Hiçbirine uymuyorsa sessizce sil
' g33_network.log
```
