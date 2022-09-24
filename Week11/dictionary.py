#Write a program that reads the words in words.txt and stores them as
#keys in a dictionary. It doesn’t matter what the values are. Then you
#can use the in operator as a fast way to check whether a string is in the
#dictionary
from random import random

empty_dictionary = dict()
fhand = open('words.txt')
for line in fhand:
    words_in_line = line.split()
    for word in words_in_line:
        empty_dictionary[word] = str(random())
        
check = input('Check for the word: ')
if check in empty_dictionary: 
    print(empty_dictionary[word])