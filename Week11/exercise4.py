#!/usr/bin/python3

#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dic-
#tionary has been created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.

fhand = open('../Week9/mbox.txt')
lst = list()
emails = dict()
most = None

for line in fhand:
    if line.startswith('From '):
        lst = line.split()
        emails[lst[1]] = emails.get(lst[1], 0) + 1
        
for entry in emails:
    #print(entry, ':', emails[entry])
    if most is None or emails[entry] > most:
        #print("DEBUG")
        #print(entry)
        #print(emails[entry])
        email = entry
        most = emails[entry]
    
print(email, most)