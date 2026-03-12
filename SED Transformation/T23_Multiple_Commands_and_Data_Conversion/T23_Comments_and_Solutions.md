# INSTRUCTIONS IN ENGLISH ------ GOREVLENDIRME TURKCE
| English Instructions | Türkçe Talimatlar |
| :--- | :--- |
| ***### Difficulty Degree:*** 4.5/5 | ***### Zorluk duzeyi:*** 4.5/10|
| SCENARIO: You’ve got a student grades list and a complex file with their absence status (g23_students.csv). In this file, you need to both correct the data format and assign "tags" to students according to certain conditions. | SENARYO:  |
| **Step 1:** Prepare the data (or download from here).  | **Adım 1:** Data Olustur (veya buradan indir).  |
| **Step 2:** MISSION | **Adım 2:** GOREV |
| 1. Format Conversion: All commas in the file (,) pipe for column separation (\|Turn to ) sign. <br><br> 2. Tagging (Append): Inside FAIL to the very end of the last lines !!!_RETAKE_EXAM_!!! add the phrase. (Hint: s/$/ yeni_metin/). <br><br> 3. Quick Deletion: Note N/A delete rows that are (not entered) completely to exclude them from analysis. <br><br> 4. Chained Operation: First 3 items single sed in command (multiple -e run it using) and the result g23_final_report.txt save as. <br><br> 5. Data Obfuscation: student_ Leaving only the first 3 letters of the student names starting with and the rest *** mask with. (Ex: student_10 -> stu***). |  |
| Analytical Question |  |
| More than one -e when you use the option, does the order of the commands change the result? (For example, first deleting commas and then trying to operate according to commas). |  |
| Analytical Question's Answer |  |
| Yes, the order changes everything. sed executes commands in the order you type them (left to right). If the first command deletes commas, the second command can no longer look for commas. Establishing this "pipeline" logic will greatly shorten your debugging time for complex scripts you write in the future |  |
| **Step 3:* SOLUTION | **Adım 2:** CEVAP |

``` bash
1. sed -E 's/,/ \| /g' g23_students.csv
2A. grep -i "FAIL" g23_A_students.csv | sed 's/$/ | !!!_RETAKE_EXAM_!!!/'

OR

2B. sed -Ei 's/(FAIL \| [0-9]{1,2})/\1 | !!!_RETAKE_EXAM_!!!/g' g23_A_students.csv
3. sed -E '/N\/A/Id' g23_A_students.csv 
4. sed -E -e 's/,/ \| /g' -e 's/(FAIL \| [0-9]{1,2})/\1 | !!!_RETAKE_EXAM_!!!/g' -e '/N\/A/Id'  g23_students.csv
5. sed -E 's/^([A-Za-z]|[a-z]{3})[A-Za-z]*_[0-9]{3}/\1***/' g23_A_students.csv 
```
