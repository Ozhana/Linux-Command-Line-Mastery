# Task

Scenario: You have a student list called students.csv. This list contains the columns Name, City, Department, and Grade.
Your task: Find the students who live in Ankara and study in the Computer department (or Computer Science).
Be careful, though: the word “Ankara” may sometimes be written as ANKARA or ankara.

1. Find the students whose lines contain both “Ankara” and “Computer”, without case sensitivity.

2. Print how many such students there are on the screen, showing only the number.

### SOLUTION
---
1. grep -i "ankara" students.csv . | grep -i "computer"
2. grep -i "ankara" students.csv . | grep -i "computer" ;echo "toplam : $(grep -i "ankara" students.csv . | grep -ic "computer")"

or

grep -i "ankara" students.csv . | grep -i "computer" | tee /dev/stderr | wc -l
