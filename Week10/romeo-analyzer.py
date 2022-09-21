fhand = open('romeo.txt')
uniq_words = list()
for line in fhand:
    words_in_line = line.split()
    for word in words_in_line:
        # .lower because otherwise But and but would each count as unique.
        if not word.lower() in uniq_words: 
            uniq_words = uniq_words + [word]
uniq_words.sort()
print(uniq_words)