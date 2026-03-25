# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 10/10 | ***### Zorluk duzeyi:*** 10/10|
| SCENARIO: now sedwe come to one of the least-known but most “dangerous” commands of: r (read). This command “injects” the contents of one file into the exact line of another file that you want. <br><br>You have a main HTML template (index.html) and then the XML data that we just generated (g38_output.xml) there is. | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Injection Point: index.html find a comment line in it that says ''. <br><br>2. Read File: sedof the r using the command, right below this comment line g38_output.xml dump the contents of its file.<br><br>3. Cleaning: Delete that ``comment line after injection (We don't need it anymore). <br><br>4. Dynamic Title: In HTML <title>...</title> update its tag to include that day's date. (You can write the date manually: 24-03-2026). |  |
| Golden Information: | Altin Bilgi: |
| r the command is a bit strange. r the file name that comes after the command is read to the end of the line, so r dosya.txt; s/../.../ you cannot perform operations like this on the same line. Usually -e it is written in separate blocks or below. |  |
| Analytical Question: | Analitik Soru: |
| Why files cat instead of combining with sed r we use? In a large web project, to print data right "in the middle" of an HTML file with thousands of lines sed what kind of surgical sensitivity does it give us? |  |
| Preparation: | Hazirlik: |
``` bash
echo "<html><head><title>Old Title</title></head>\
<body><h1>Report</h1></body></html>" > index.html
```

| **Step 3:* SOLUTION | **Adım 3:** CEVAP |

``` bash
sed -Ee ‘r g39_output.xml’ -e “s/<title>.*<\/title>\
/<title>Report - $(date +%d-%m-%Y)<\/title>/” g39_index.html
```
