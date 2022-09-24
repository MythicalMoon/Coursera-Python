#!/usr/bin/python3

#Exercise 5: This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the contents of your dictionary.

fhand = open('../Week9/mbox-short.txt')
words_in_line = list()
domain = dict()

for line in fhand:
    if line.startswith('From '):
        words_in_line = line.split()
        for word in words_in_line:
           if '@' in word:
               email = word
               usr_domain = email.split('@')
               domain[usr_domain[1]] = domain.get(usr_domain[1], 0) + 1

print(domain)