# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/10 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: You have daily sales data of a market (g27_sales_raw.csv). However, the data is in a structure called "Long Format", where each process is written one under the other. Before putting this data from you into an analysis tool sed just clean it with Product Name and Total Sales (Pieces x Price) you are asked to simplify it as follows. | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Arithmetic Preparation: In every line ADET:5 | FIYAT:10 there is a structure like this. sed he can't do math, but you put the data into a format like this: URUN_ADI -> (5*10). <br><br> 2. Fly Unnecessary Columns: Completely delete columns such as sales representative name and branch code. <br><br> 3. Category Labeling: If the product name is in it PRO_ If (Professional Series) is mentioned, at the beginning of the line [PREMIUM] add tag. <br><br> 4. Sequential Cleaning: The first 2 lines (headings) and the last line (subsum of totals) in the file should be excluded from analysis. <br><br> 5. Advanced Filtering: Only PREMIUM what is and the price 50 leave products with more than units on the screen and delete the others. |  |
| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash

```
