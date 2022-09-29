#!/usr/bin/python3

#Exercise 3: Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at 

import string

fhand = open('../Week11/romeo.txt')
words_in_line = dict()
counter = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.translate(str.maketrans('', '', string.digits))
    line = line.translate(str.maketrans('', '', string.whitespace))
    line = line.lower()
    
    for letter in line:
        counter[letter] = counter.get(letter, 0) + 1
        
lst = list(counter.items())
lst.sort()

#counter for percentage converter
count = 0
for ltr, cnt in lst[:]:
    count = count + cnt

#prints frequency with percentages
for ltr, cnt in lst[:]:
    percent = cnt / count
    percent = str(percent)
    
    print(ltr, cnt, 'or', int(percent[2:4]), '%')