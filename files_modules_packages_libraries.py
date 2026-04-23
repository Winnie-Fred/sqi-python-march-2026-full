# with open("for_loops.py", "r") as f:
#     # contents = f.read()
#     lines = f.readlines()


# print(contents)
# print(lines)

# for idx, line in enumerate(lines, start=1):
#     print(f"Line {idx}", line)

# with open("new_file.txt", "w") as f:
#     f.write("This line was written using Python")


# with open("new_file.txt", "a") as f:
#     f.write("This is another line that was written using Python\n")


# f = open("new_file.txt", "r")
# print(f.read())
# f.close()

# module - python file, usually part of a larger package.
# script - python file that has a single responsibility and is not needed after that responsibility is fulfilled. It is not usually part of a larger program/package.
# package - a folder containing python modules usually with an __init__.py file.

# Assignment 2.
# ------------------------------------------------------------
# 1. Read All Lines and Count Them
# ------------------------------------------------------------
# There is a file called "students.txt" with the following content:
#
# Alice
# Bob
# Charlie
# David
#
# Task:
# - Read all lines from the file.
# - Print the total number of students.
#
# Sample Execution:
# > python program.py
#
# Expected Output:
# Total students: 4



# ------------------------------------------------------------
# 2. Convert All Names to Uppercase and Save
# ------------------------------------------------------------
# File: "names.txt"
#
# john
# mary
# peter
#
# Task:
# - Read all names.
# - Convert each name to uppercase.
# - Write them into a new file called "uppercase_names.txt".
#
# After running the program,
# the new file should contain:
#
# JOHN
# MARY
# PETER


# with open("names.txt", "r") as f:
#     contents = f.read()


# with open("uppercase_names.txt", "w") as f:
#     f.write(contents.upper())



# ------------------------------------------------------------
# 3. Remove Empty Lines
# ------------------------------------------------------------
# File: "data.txt"
#
# Apple
#
# Banana
#
# Orange
#
# Task:
# - Read all lines.
# - Remove empty lines.
# - Write the cleaned result into "cleaned_data.txt".
#
# Expected file content:
#
# Apple
# Banana
# Orange



# ------------------------------------------------------------
# 4. Count Words in File
# ------------------------------------------------------------
# File: "story.txt"
#
# Python is fun
# Coding is powerful
#
# Task:
# - Read the file.
# - Count the total number of words.
# - Print the total.
#
# Sample Execution:
# > python program.py
#
# Expected Output:
# Total words: 6



# ------------------------------------------------------------
# 5. Append a New Log Entry
# ------------------------------------------------------------
# File: "log.txt"
#
# System started
#
# Task:
# - Append a new line that says: "User logged in"
#
# Expected file content after running:
#
# System started
# User logged in



# ------------------------------------------------------------
# 6. Reverse Each Line
# ------------------------------------------------------------
# File: "words.txt"
#
# cat
# dog
# fish
#
# Task:
# - Read each line.
# - Reverse the letters.
# - Save results into "reversed_words.txt".
#
# Expected content:
#
# tac
# god
# hsif

# with open("words.txt", "r") as f:
#     lines = f.readlines()

# reversed_lines = [line.strip()[::-1] + "\n" for line in lines]
# reversed_lines = "".join(reversed_lines)
# print(reversed_lines)

# with open("reversed_words.txt", "w") as f:
#     f.write(reversed_lines)

# ------------------------------------------------------------
# 7. Add Line Numbers
# ------------------------------------------------------------
# File: "tasks.txt"
#
# Wash dishes
# Do homework
# Clean room
#
# Task:
# - Read the file.
# - Add numbers at the beginning of each line.
# - Save into "numbered_tasks.txt".
#
# Expected content:
#
# 1. Wash dishes
# 2. Do homework
# 3. Clean room



# ------------------------------------------------------------
# 8. Filter Numbers Greater Than 50
# ------------------------------------------------------------
# File: "numbers.txt"
#
# 12
# 75
# 30
# 88
#
# Task:
# - Read all numbers.
# - Keep only numbers greater than 50.
# - Write them into "big_numbers.txt".
#
# Expected content:
#
# 75
# 88



# ------------------------------------------------------------
# 9. Replace a Word
# ------------------------------------------------------------
# File: "message.txt"
#
# I love cats
#
# Task:
# - Replace the word "cats" with "dogs".
# - Save result into "updated_message.txt".
#
# Expected content:
#
# I love dogs



# ------------------------------------------------------------
# 10. Merge Two Files
# ------------------------------------------------------------
# File 1: "first.txt"
#
# A
# B
#
# File 2: "second.txt"
#
# C
# D
#
# Task:
# - Read both files.
# - Combine their contents.
# - Write into "merged.txt".
#
# Expected content:
#
# A
# B
# C
# D
# ============================================================

# from datetime import datetime

# now = datetime.now()

import datetime

# now = datetime.datetime.now()

# print(now)


# sixteenth_mar_2025 = datetime.date(2025, 3, 16)
# print(sixteenth_mar_2025)

# one_week = datetime.timedelta(weeks=1)

# one_week_after_sixteenth = sixteenth_mar_2025 + one_week
# print(one_week_after_sixteenth)

# 23/03/2025

# strptime -> string parse time (str -> date)
# strftime -> string format time (date -> str)

# one_week_after_sixteenth_str = one_week_after_sixteenth.strftime("%Y-%m-%d")
# print(one_week_after_sixteenth_str)

# now_formatted = now.strftime("%Y/%m/%d %H:%M:%S")
# print(now_formatted)

# date_str = "23 February, 2024"
# date = datetime.datetime.strptime(date_str, "%d %B, %Y")
# print(date)
# print(date + datetime.timedelta(3))


# 23 February
# February 23
# Feb 23
# 23/02
# 23-02