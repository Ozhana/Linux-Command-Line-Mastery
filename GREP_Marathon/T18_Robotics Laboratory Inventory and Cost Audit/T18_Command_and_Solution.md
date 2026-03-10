# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/5|
| SCENARIO: Keeping a list of parts in the laboratory g18_inventory.txt you have a file. The format is: <br> PARCA_ADI:STOK_ADEDI:BIRIM_FIYAT:KATEGORI <br><br> Example: HC-SR04:12:45.50:Sensor | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Only Sensor or Motor find tracks in category.<br><br>2. Stock quantity single digit Filter parts (between 1-9) (that is, those that have dropped to critical levels in stock). <br> Hint: : you should focus on the number between your signs. Regex: :[1-9]: <br><br> 3. These are critical parts by price (3rd column) sort from largest to smallest. <br> Attention: sort at command -t (separator) and -k (column) parameters, also for numerical sorting -n and for reverse sorting -r you will need to use it. <br><br> 4. Challenging Bonus: After all, just PARCA_ADI and the BIRIM_FIYAT let it be seen, an arrow in between (->Print by putting ).<br> Hint: cut take the parts with sed or you can combine it with a simple loop, but just for now cut -d':' -f1,3 just bring it side by side with. |  |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash

```
