import re

hand = open('../Week9/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('\S+@\S+', line)
    if len(x) > 0:
        print(x)
        
#problem here is that it spits out strings with < , ; or other symbols