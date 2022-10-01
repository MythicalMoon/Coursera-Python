#!/usr/bin/python3

#Exercise 2: Write a program to look for lines of the form:

#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average as an integer.

import re

rev = list()
average_rev = 0

fhand = open('../Week9/mbox.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    for match in x:
        match = float(match)
        rev = rev + [match]

sum_rev = sum(rev)
count = float(len(rev))
average_rev = sum_rev / count
print(int(average_rev))