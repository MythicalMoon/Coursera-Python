#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the num-
#ber of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits

import string

fhand = open('../Week9/mbox.txt')
words_in_line = list()
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words_in_line = line.split()
        for word in words_in_line:
           if '@' in word:
               email = word
               counts[email] = counts.get(email, 0) + 1
               
#creates list of counts key and values and reverse sorts
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
    
lst.sort(reverse=True)

#prints Highest value
for key, val in lst[:1]:
    print(val, key)
