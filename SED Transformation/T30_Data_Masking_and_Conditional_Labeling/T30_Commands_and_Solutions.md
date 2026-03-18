# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: In your hand g30_customers.csv has file. File format: NAME \| EMAIL \| TOTAL_SPEND \| COUNTRY.<br><br>You are asked to both secure this data and turn it into a "Marketing Report". | SENARYO: Elinizde g30_customers.csv dosyası var. Dosya formatı: NAME \| EMAIL \| TOTAL_SPEND \| COUNTRY. <br><br>Sizden bu veriyi hem güvenli hale getirmeniz hem de bir "Pazarlama Raporu"na dönüştürmeniz isteniyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
|1. Email Anonymization: Only the first 2 letters of the emails and @ leave the interval after the sign *** close with. (Ex: ozhan@mail.com -> oz***@mail.com)<br><br>2. Dynamic Segmentation:<br><br>-If TOTAL_SPEND If greater than 5000, per line [VIP_GOLD] add.<br><br>-If between 1000-5000, the [SILVER] add.<br><br>-If it is less than 1000, do not add anything.<br><br>3. Country Coding: Country names (Ex: Qatar, the Turkey) shorten only the first 3 letters to capitalize (Ex: QAT, the TUR).<br><br>4. Hold Space Mastery: Try to add under each segment (GOLD, SILVER) as a counter how many customers belong to that segment (This is optional, if you cannot do it, only segmentation is sufficient).<br><br>5. Final Touch: Output marketing_ready.txt save as. |1. Email Anonimleştirme: E-postaların sadece ilk 2 harfini ve @ işaretinden sonrasını bırakın, arayı *** ile kapatın. (Örn: ozhan@mail.com -> oz***@mail.com)<br><br>2.Dinamik Segmentasyon:<br><br>- Eğer TOTAL_SPEND 5000'den büyükse, satırın başına [VIP_GOLD] ekleyin.<br><br>- Eğer 1000-5000 arasındaysa, [SILVER] ekleyin.<br><br>- 1000'den küçükse hiçbir şey eklemeyin.<br><br>3. Ülke Kodlama: Ülke isimlerini (Örn: Qatar, Turkey) sadece ilk 3 harfi büyük olacak şekilde kısaltın (Örn: QAT, TUR).<br><br>4. Hold Space Mastery: Her segmentin (GOLD, SILVER) altına o segmente ait kaçıncı müşteri olduğunu bir sayaç gibi eklemeye çalışın (Bu opsiyoneldir, yapamazsanız sadece segmentasyon yeterli).<br><br>5. Final Dokunuş: Çıktıyı marketing_ready.txt olarak kaydedin. |
| Golden Information: | Altin Bilgi: |
| sed in the \U Remember the (Uppercase) operator: s/(...).*/\U\1/ the expression captures the first 3 letters and converts them to uppercase letters. | sed içinde \U (Uppercase) operatörünü hatırlayın: s/(...).*/\U\1/ ifadesi ilk 3 harfi yakalar ve onları büyük harfe çevirir. |
| Analytical Question: | Analitik Soru: |
| To capture numbers greater than 5000 in this mission / \| [5-9][0-9]{3} \| / we used a regex like this. Well the number is exactly 10000 If there were (5 digits), would this regex work? As the number digit changes sed what are the risks of performing numerical analysis with? | Bu görevde 5000'den büyük sayıları yakalamak için / \| [5-9][0-9]{3} \| / gibi bir regex kullandık. Peki sayı tam olarak 10000 (5 hane) olsaydı bu regex çalışır mıydı? Sayı hanesi değiştikçe sed ile sayısal analiz yapmanın riskleri nelerdir? |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -E '
# 1. Email Maskeleme (ozhan@ -> oz***@)
s/(\| [^@]{2})[^@]+@/\1***@/

# 2. Segmentasyon (Önce GOLD sonra SILVER, çakışmayı önlemek için ! etiketi)
/[|] [5-9][0-9]{3} [|]/ s/^/[VIP_GOLD] /
/^\[VIP_GOLD\]/! { /[|] [1-4][0-9]{3} [|]/ s/^/[SILVER] / }

# 3. Ülke Kısaltma ve Büyük Harf (Japan -> JAP)
s/\| ([[:alpha:]]{3})[[:alpha:]]+$/| \U\1/

' g30_customers.csv > marketing_ready.txt
```
