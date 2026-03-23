# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 9/10 | ***### Zorluk duzeyi:*** 9/10|
| SCENARIO: You have a list of financial transactions (g36_transactions.log). Some transactions are "Suspicious" (SUSPICIOUSMarked as ), some as "Approved" (APPROVED). | SENARYO: Elinizde bir finansal işlem listesi var (g36_transactions.log). Bazı işlemler "Şüpheli" (SUSPICIOUS) olarak işaretlenmiş, bazıları ise "Onaylanmış" (APPROVED). |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Quantity Analysis: If the transaction amount (Amount) 5000IF LESS THAN AND status APPROVED if so, delete this line from the report (Because we are not interested in small and approved transactions). <br><br>2. Critical Protection: If transaction SUSPICIOUS NEVER delete it, regardless of the amount.<br><br>3. Emphasis: In the remaining lines SUSPICIOUS the word [!!! ALERT !!!] replace with. <br><br>4. Format: ID: [ID] - AMT: [AMOUNT] maintain the structure in shap | 1. Miktar Analizi: Eğer işlem miktarı (Amount) 5000'den küçükse VE durum APPROVED ise bu satırı rapordan silin (Çünkü küçük ve onaylı işlemlerle ilgilenmiyoruz). <br><br>2. Kritik Koruma: Eğer işlem SUSPICIOUS ise, miktarı ne olursa olsun ASLA silmeyin.<br><br>3. Vurgu: Kalan satırlarda SUSPICIOUS kelimesini [!!! ALERT !!!] ile değiştirin.<br><br>4. Format: ID: [ID] - AMT: [AMOUNT] şeklindeki yapıyı koruyun |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
| sed why is the order of its commands vital? Before SUSPICIOUS what happens if you change the word and then delete it? | sed komutlarının sırası neden hayati önem taşır? Önce SUSPICIOUS kelimesini değiştirip sonra silme işlemi yaparsanız ne olur? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee '/APPROVED/{/AMT: [1-4][0-9]{1,3}/d}; \
/SUSPICIOUS/s/^/\[!!!_ALERT_!!!\] /g; s/^ID/ ID/g' g36_transactions.log | column -ts ' '
```
