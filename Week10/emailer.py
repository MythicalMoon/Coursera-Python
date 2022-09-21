hand = open('../Week9/mbox-short.txt')
count = 0
for line in hand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or len(words) < 2 : continue
    if words[0] != 'From' : continue
    print(words[1])
    count = count + 1
print('There were', count, 'lines in the file with From as the first word')
