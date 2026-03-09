### Difficulty Degree: 2/5

Situation: You are working on an Arduino project or have a configuration file.
The file is very crowded; dozens of empty lines and # or // There are comment lines starting with.
You need to clear this "noise" to see the real code (i.e. useful data).

### Step 1: Prepare Data
This is Python code for you project.ino it will give you a file called, full of spaces and comments.

### Step 2: Task
---
project.ino in his file empty lines one that won't show grep type command.

Then, both the blank lines and // starting with comment lines just press the "clean code" on the screen by eliminating it.

---

Submit Billi: * Empty line regex'te ^$ (line head and line end adjacent) is performed ifade.

For the process of "eliminating" or "not including" something -v let me remind you that you should use (invert-match).

// characters may require an escape character on some systems,
but they are in quotes when searching in plain text "//" it will do its job.
