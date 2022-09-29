#Exercise 2: This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.

fhand = open('../Week9/mbox-short.txt')
words_in_line = list()
hours = dict()

for line in fhand:
    if line.startswith('From '):
        words_in_line = line.split()
        for word in words_in_line:
           if ':' in word:
               time_stamps = word.split(':')
               hours[time_stamps[0]] = hours.get(time_stamps[0], 0) + 1

lst = list()
for key, val in list(hours.items()):
    lst.append((key, val))
    
lst = list(hours.items())
lst.sort()

for hour, count in lst[:]:
    print(hour, count)
               