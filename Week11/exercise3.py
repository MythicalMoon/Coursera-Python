#!/usr/bin/python3

#Exercise 3: Write a program to read through a mail log, build a his-
#togram using a dictionary to count how many messages have come from
#each email address, and print the dictionary.

fhand = open('../Week9/mbox-short.txt')
lst = list()
emails = dict()

for line in fhand:
    if line.startswith('From '):
        lst = line.split()
        emails[lst[1]] = emails.get(lst[1], 0) + 1
        
print(emails)