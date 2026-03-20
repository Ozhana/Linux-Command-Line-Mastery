# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: You have a very dirty file (g32_dirty_data.csv). At the beginning and end of the lines, there are endless “garbage” characters (dots, commas, dashes, spaces) no matter how many times you clear them. s/^[ ,.-]+//g sometimes, in complex arrays (for example, a dot after a gap, and a gap after a dot), it may not be able to clear them all at once | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Define Tag: :temizle select a starting point named.<br><br>2. Surgical Cleaning: At the beginning of the line (^) and at the end ($) all  , the ., the ,, the - one character s/// delete with.<br><br>3. Loop Setup (The Branch): t temizle use command. (This command means: "If you just deleted something, go back to the beginning and look again").<br><br>4. Conclusion: Until the line becomes completely smooth sed it will spin within itself and when it is finished, it will be in its clean state.<br><br>5. Filter: If the line is completely empty when cleaning is finished, do not print that line. |  |
| Golden Information: | Altin Bilgi: |
|  |  |
| Analytical Question: | Analitik Soru: |
| As a data analyst; Why is it safer to do a little cleaning and set up a loop that says "go back to square one until everything is clear" instead of writing a single giant regex? What does the cycle give us in complex and unpredictable dirty data? |  |
| Answer of Analytical Question: | Analitik Sorunun Cevabi: |
| What I ask is "Why loop instead of a single regex?" the answer to the question is <br><br>**"Unpredictable Layers"**. <br><br>Let's say your data is like this:  ...- -...DATA...- -... <br><br>A single global regex (s/^[ .-]+//gWhen you type ), the regex engine looks at the beginning of the line, deletes the matching group, and stops. If under the deleted part new one if the dirty layer appears (for example, new spots that appear after the gaps are erased), a standard s/// sometimes you may miss these or it requires you to write a very complex regex. |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
