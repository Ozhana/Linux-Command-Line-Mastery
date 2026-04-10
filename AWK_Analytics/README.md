# 🐧 AWK Analytics & Data Mastery

Welcome to the **AWK Analytics** module of the Linux Command Line Mastery series. This repository is a comprehensive journey from a "Mathematics Teacher" perspective into the world of high-performance text processing and data analysis using **AWK**.

> "AWK is not just a command; it's a language for those who see patterns in chaos."

---

## 🎓 The Curriculum: From Basics to Big Data (60 Lessons)

This roadmap is divided into 4 strategic phases, designed to transform a terminal user into a data processing expert.

### 📍 Phase 1: The Foundations (Lessons 1-15)
- [x] **01:** Basic Print and Field Extraction
- [x] **02:** Using Beginners: `BEGIN` and `END` Blocks
- [x] **03:** Field Separators (`-F`, `FS`)
- [x] **04:** Conditional Logic (If/Else) inside AWK
- [x] **05:** Pattern Matching with Regex
- [ ] **06-15:** Arithmetic Operations, Logical Operators, and Built-in Variables (`NR`, `NF`).

### 📍 Phase 2: Flow Control & Record Management (Lessons 16-30)
- [x] **16:** Record Separators (`RS`) & Multi-line Records
- [x] **17:** Output Field/Record Separators (`OFS`, `ORS`)
- [x] **18:** Looping Structures (`for`, `while`)
- [x] **19:** Working with Multiple Files (`NR == FNR` Logic)
- [x] **20:** Passing External Variables (`-v`)
- [ ] **21-30:** Advanced Pattern Ranges, Next/Exit commands, and System Integration.

### 📍 Phase 3: Advanced Data Structures (Lessons 31-45)
- [x] **31:** User-Defined Functions (`function`)
- [x] **32:** Associative Arrays (The heart of AWK)
- [ ] **33:** Multidimensional Arrays (Matrix Processing)
- [ ] **34:** String Manipulation Functions (`split`, `substr`, `gsub`)
- [ ] **35:** Mathematical Functions (`sin`, `cos`, `sqrt`, `rand`)
- [ ] **36-45:** Data Cleaning techniques, Handling Anomalies, and Pivot Table Simulations.

### 📍 Phase 4: Expert Level & Real-World Projects (Lessons 46-60)
- [ ] **46:** Network Log Analysis (Security Auditing)
- [ ] **47:** Financial Report Generation
- [ ] **48:** Integrating AWK with Shell Scripts
- [ ] **49:** Performance Tuning for Giga-Scale Files
- [ ] **60:** **Final Capstone:** Building a complete CLI Data Dashboard.

---

## 🛠️ Tech Stack & Environment
- **OS:** Fedora 43 (Workstation) / Windows 11 (Dual Boot)
- **Hardware:** Surface Pro 9
- **Scripting:** AWK (Gawk), Python (for Data Generation)

---

## 🚀 How to Use These Labs
Each lab folder contains:
1. `gXX_generator.py`: A Python script to generate large-scale, "dirty" datasets (500-1000+ lines).
2. `gXX_answer.awk`: The AWK script solving the specific data challenge.
3. `README.md`: Explanation of the logic and mathematical approach.

Example Command:
```bash
awk -v dep="Math" -f g12_matrix_report.awk g12_big_data.csv
```
## 👨‍🏫 About the Author
Dr. Ozhan Akdag

PhD in Mathematics & PhD in Education.

Mathematics Teacher & Freelance Data Analyst.

Robotics Club Manager & Linux Enthusiast.

Exploring the intersection of Pure Mathematics and Cybersecurity through the Linux Terminal.

## ⚖️ License
This project is licensed under the MIT License - see the LICENSE file for details.
