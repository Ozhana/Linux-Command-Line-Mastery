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
| Gemini said:
Sir, this is the solution "stable and safe" it was an engineering approach. Especially the first sed put the data into a standard comma format (CSV) and second sed a method that reduces the margin of error to zero by "collecting fruits" (swap process).

But to the next level, that is "sed Ninja" do this in a single move (one by one to get to the level s/// I would like you to do it with the command). Why? Because in large data sets "pipe" (|using ) creates an additional cost when moving data from one process to another.

Come and share those clean regex groups you wrote in one place sed in it, let’s combine it with any order you like:

G35: One-Move "Grand Master" Solution
Bash
sed -Ee 's/^\[([0-9:]+)\][[:space:]-]+([[:alpha:]_0-9]+):[[:space:]]+([0-9.]+)[[:space:]]+\(([[:alpha:]]+)\)/\U\2 | \3 | \4 | [\1]/' g35_sensors.csv
Differences with your code:

Sorting Freedom: \2 | \3 | \4 | [\1] with his formation, we put the groups in the seat we wanted as soon as we caught them. Second one sedThere is no need for.

\U\2: Sensor ID (\2) We put it on his head while pressing \U, he capitalized the entire group.

Speed: Data is read only once and written once.

Answer to Analytical Question: The Danger of "Greedy" (Greedy)
What I ask is "What would happen if there was a gap in the sensor name?" the answer to the question is:
If in regex (.*) if you use, sed it goes all the way to the very end of the line and then comes back looking for matches. If there is a space in the sensor name and you (.*) if you try to capture with (regex that space or the next two points:) the group may be surprised to get the limit.

In your solution ([[:alpha:]_[:digit:]]+) using specific your definition of a class was a very professional move that curbed "greed".

Task 36: "Conditional Line Deletion" (Logical Line Destruction)
Difficulty Level: 9 / 10

Sir, now sed"deletion" of (d) his talent, like a data analyst conditional let's use. It is easy to delete just one word; but it is difficult to delete a "if condition does not occur".

Scenario:
You have a list of financial transactions (g36_transactions.log). Some transactions are "Suspicious" (SUSPICIOUSMarked as ), some as "Approved" (APPROVED).

Requests:

Quantity Analysis: If the transaction amount (Amount) 5000IF LESS THAN AND status APPROVED if so, delete this line from the report (Because we are not interested in small and approved transactions).

Critical Protection: If transaction SUSPICIOUS NEVER delete it, regardless of the amount.

Emphasis: In the remaining lines SUSPICIOUS the word [!!! ALERT !!!] replace with.

Format: ID: [ID] - AMT: [AMOUNT] maintain the structure in shape.

Python Data Generator: g36_generator.py
Python
import random

def generate_g36_data():
    statuses = ["APPROVED", "PENDING", "SUSPICIOUS"]
    with open("g36_transactions.log", "w") as f:
        for i in range(100, 140):
            status = random.choice(statuses)
            amt = random.randint(100, 9999)
            f.write(f"ID: {i} - STATUS: {status} - AMT: {amt}\n")

if __name__ == "__main__":
    generate_g36_data()
    print(">>> 'g36_transactions.log' üretildi. Filtreleme başlasın!")
Strategic Tip:
Sir, you will need to do "Negative Filtering" here. sedin the !d (delete if not matching) or /regex/d you must string the (delete if matched) commands in a logical order.

Analytical Question:
sed why is the order of its commands vital? Before SUSPICIOUS what happens if you change the word and then delete it? | sed komutlarının sırası neden hayati önem taşır? Önce SUSPICIOUS kelimesini değiştirip sonra silme işlemi yaparsanız ne olur? |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee '/APPROVED/{/AMT: [1-4][0-9]{1,3}/d}; \
/SUSPICIOUS/s/^/\[!!!_ALERT_!!!\] /g; s/^ID/ ID/g' g36_transactions.log | column -ts ' '
```
