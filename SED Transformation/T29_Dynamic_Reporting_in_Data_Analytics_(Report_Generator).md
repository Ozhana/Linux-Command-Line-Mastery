# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: You have a system error report (g29_system.log). In this file sometimes "System Status" (STATUS: ...) sometimes "Mistakes" (ERROR: ...) writes. What is requested from you; last seen STATUS keep your knowledge in mind and keep it in mind ERROR create a report that adds the current status to the beginning of the line. | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Using Hold Space (h, the g, the x): * h (Hold): Copies the pattern space into the drawer. <br>- g(Get): Returns what's in the drawer to pattern space. <br><br>2. Logic: In line STATUS if it does pass, throw it in the drawer (h). In line ERROR if it does, take the status in the drawer with you (G) and combine the two in one line.<br><br>3. Cleaning: Print only lines containing ERROR (with status next to it).<br><br>4. Format: The output should be like this: [Current Status: OK] -> ERROR: Database_Timeout <br><br>5. Filter: Do not report (delete) errors with "Low" in them. |  |
| Golden Information: | Altin Bilgi: |
|  |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
