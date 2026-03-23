# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 9/10 | ***### Zorluk duzeyi:*** 9/10|
| SCENARIO: You have a sensor data (g35_sensors.csv). The format is a bit strange:<br>[SAAT] - SENSOR_ID: DEGER (BIRIM)<br><br>Example: [14:30] - TEMP_01: 25.4 (Celsius)<br><br>You are asked to convert this data to a professional CSV format. | SENARYO: Elinizde bir sensör verisi var (g35_sensors.csv). Formatı biraz garip:<br>[SAAT] - SENSOR_ID: DEGER (BIRIM)<br><br>Örnek: [14:30] - TEMP_01: 25.4 (Celsius) <br><br>Sizden bu veriyi profesyonel bir CSV formatına dönüştürmeniz isteniyor. |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Group Capture: Catch 4 separate groups with Regex: SAAT, the SENSOR_ID, the DEGER, the BIRIM. <br><br>2. Relocation (Swap): Bring the output to the following format: SENSOR_ID | DEGER | BIRIM | [SAAT].<br><br>3. Cleaning: Completely eliminate parentheses and unnecessary dashes. <br><br>4. Uppercase Letter: SENSOR_ID force all letters in the section to uppercase (\U reminder). | 1. Grup Yakalama: Regex ile 4 ayrı grubu yakalayın: SAAT, SENSOR_ID, DEGER, BIRIM. <br><br>2. Yer Değiştirme (Swap): Çıktıyı şu formata getirin: SENSOR_ID | DEGER | BIRIM | [SAAT]. <br><br>3. Temizlik: Parantezleri ve gereksiz tireleri tamamen yok edin. <br><br>4. Büyük Harf: SENSOR_ID kısmındaki tüm harfleri büyük harfe zorlayın (\U hatırlatması). |
| Golden Information: | Altin Bilgi: |
| \( and the \) when separating groups with fixed characters (space, hyphen, colon) of the group outside be careful to let go.

Sample template: s/\[(.*)\] - (.*): (.*) \((.*)\)/\2 | \3 | \4 | [\1]/ | \( ve \) ile grupları ayırırken aradaki sabit karakterleri (boşluk, tire, iki nokta) grubun dışında bırakmaya dikkat edin.

Örnek şablon: s/\[(.*)\] - (.*): (.*) \((.*)\)/\2 | \3 | \4 | [\1]/ |
| Analytical Question: | Analitik Soru: |
| If there was a space in the sensor name (Ex: Living Room Temp), in your regex (.*) could it be dangerous to use? Where does "greedy" (greedy) regex behavior cause us to make mistakes when breaking down this data? | Eğer sensör isminde de boşluk olsaydı (Örn: Living Room Temp), sizin regex'inizde (.*) kullanımı tehlikeli olabilir miydi? "Greedy" (açgözlü) regex davranışı, bu veriyi parçalarken nerede hata yapmamıza sebep olur? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
| What I ask is "What would happen if there was a gap in the sensor name?" the answer to the question is:
If in regex (.*) if you use, sed it goes all the way to the very end of the line and then comes back looking for matches. If there is a space in the sensor name and you (.*) if you try to capture with (regex that space or the next two points:) the group may be surprised to get the limit. | Sorduğum "Sensör isminde boşluk olsaydı ne olurdu?" sorusunun cevabı şudur:
Eğer regex içinde (.*) kullanırsanız, sed satırın en sonuna kadar gider ve sonra geri gelerek eşleşme arar. Eğer sensör isminde boşluk varsa ve siz (.*) ile yakalamaya çalışırsanız, regex o boşluğu mu yoksa bir sonraki iki noktayı mı (:) grup sınırı alacağını şaşırabilir. |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee 's/^\[([0-9:]+)\][[:space:]-]+([[:alpha:]_0-9]+):[[:space:]]+([0-9.]+)[[:space:]]+\(([[:alpha:]]+)\)/\U\2 | \3 | \4 | [\1]/' g35_sensors.csv
```
