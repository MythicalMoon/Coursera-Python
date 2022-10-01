#!/usr/bin/python3

#Exercise 1: Write a simple program to simulate the operation of the
#grep command on Unix. Ask the user to enter a regular expression and
#count the number of lines that matched the regular expression:

import re

fhand = open('../Week9/mbox.txt')
prompt = "Enter regular expression: "
query = input(prompt)
count = 0

for line in fhand:
    line = line.rstrip()
    if re.findall(query, line) != []:
        count += 1
    
print(count)