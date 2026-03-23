# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: You have a secret message in your hand (g34_secret.txt). You are asked to scroll this message with a simple "Caesar Encryption" (ROT1) logic. Well; A when you see it B, the B when you see it C a system that will. | SENARYO: Elinizde gizli bir mesaj var (g34_secret.txt). Sizden bu mesajı basit bir "Sezar Şifrelemesi" (ROT1) mantığıyla kaydırmanız isteniyor. Yani; A gördüğünde B, B gördüğünde C yapacak bir sistem. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. y Use Command: sed'in is little known but very powerful y/kaynak/hedef/ investigate command. <br><br>2. Conversion: Convert all lowercase and uppercase letters in the alphabet to the next letter (a->b, the z->a, the A->B, the Z->A). <br><br>3. Figures: Shift the numbers as well (0->1, the 9->0).<br><br>4. Application: Encrypt the "Top Secret" message I will give you with this command. <br><br>Message: Your name Your future plans - Year: 2026 | 1. y Komutunu Kullanın: sed'in az bilinen ama çok güçlü y/kaynak/hedef/ komutunu araştırın. <br><br>2. Dönüşüm: Alfabedeki tüm küçük ve büyük harfleri birer sonraki harfe dönüştürün (a->b, z->a, A->B, Z->A). <br><br>3. Rakamlar: Rakamları da kaydırın (0->1, 9->0). <br><br>4. Uygulama: Size vereceğim "Çok Gizli" mesajı bu komutla şifreleyin. <br><br>Mesaj: YorName -your future plans - Year: 2026 |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
| s/a/b/g; s/b/c/g; ... 26 in a row s why one instead of typing the command y/abc.../bcd.../ should we use the command? If one after another s if you used it, first afrom the bThe character that turns into is the next s/b/c/g again at command cWould it turn into? How does this “chain reaction” break data security? | s/a/b/g; s/b/c/g; ... şeklinde peş peşe 26 tane s komutu yazmak yerine neden tek bir y/abc.../bcd.../ komutu kullanmalıyız? Eğer peş peşe s kullansaydınız, ilk a'dan b'ye dönüşen karakter, bir sonraki s/b/c/g komutunda tekrar c'ye dönüşür müydü? Bu "zincirleme reaksiyon" veri güvenliğini nasıl bozar? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
| I asked "Why s/// we don't use it?" you actually gave the technical answer to the question with your application. y command "Transliteration" it does. That is, it scans the line once and instantly replaces each character with its counterpart on the target. s/// it runs sequentially (sequential); This creates an unwanted "chain reaction" (cascade effect) in the data and breaks the encryption. | Sorduğum "Neden s/// kullanmıyoruz?" sorusunun teknik cevabını aslında uygulamanızla verdiniz. y komutu "Transliteration" yapar. Yani satırı bir kez tarar ve her karakteri hedefteki karşılığıyla anında değiştirir. s/// ise ardışık (sequential) çalışır; bu da veride istenmeyen bir "zincirleme reaksiyon" (cascade effect) yaratır ve şifrelemeyi bozar. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
echo "Dr. Ozhan Akdag - Code: 99-AZ" | sed 'y/123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/234567891bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA/'
```
