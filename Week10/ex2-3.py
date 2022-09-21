#Exercise 3: Rewrite the guardian code in the above example without
#two if statements. Instead, use a compound logical expression using
#the or logical operator with a single if statement.

hand = open('../Week9/mbox-short.txt')
count = 0
for line in hand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or len(words) < 3 : continue
    if words[0] != 'From' : continue
    print(words[2])
    
#remember that running this code in a IDE will error out, but 
#doing it from the terminal it'll work, just remember to chmod +x
