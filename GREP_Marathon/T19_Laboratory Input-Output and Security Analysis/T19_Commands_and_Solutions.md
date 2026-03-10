# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: Entry-exit logs of the laboratory door g19_access_logs.txt it is kept in his file. Format: <br> GÜN-AY-YIL SAAT:DAKİKA:SANİYE | KULLANICI_ID | İŞLEM | KAPI_DURUMU <br> Example: 10-03-2026 14:20:15 | USER_45 | ENTRY | SUCCESS | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only afternoon (hour 12:00:00 with 17:59:59 find transactions taking place between). <br> Hint: Focus on the beginning of the clock part: 1[2-7]: <br><br> 2. Between these hours faulty find login attempts (Process ENTRY it will happen, but Door Status FAIL will be). <br><br> 3. Challenging Part: Which user (USER_XX) find out how many times you received "FAIL" and sort from most to least error. <br><br> 4. Final Touch (Bash): Can you print the ID of the first 3 users who made the most mistakes on the screen as "SUSPECT LIST: ID1, ID2, ID3" (in a single line)? (Hint: head -n 3 and the paste -sd "," or you can use loop). |  |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash

```
