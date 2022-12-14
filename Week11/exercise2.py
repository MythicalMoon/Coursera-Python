#Exercise 2: Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter)

fhand = open('../Week9/mbox-short.txt')
words_in_line = list()
days = dict()
for line in fhand:
    if line.startswith('From '):
        words_in_line = line.split()
        days[words_in_line[2]] = days.get(words_in_line[2], 0) + 1
        
print(days)