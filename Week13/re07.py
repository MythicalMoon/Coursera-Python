import re
hand = open('../Week9/mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        print(x)
        
# a fix for re06, to specificy that the expression we're looking for
# needs to start with a letter or number and end with letter or num.