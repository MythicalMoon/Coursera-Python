fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word.lower() not in counts:
            counts[word.lower()] = 1
        else:
            counts[word.lower()] += 1
            
lst = list(counts.keys())
lst.sort()

#sorted printing from list
for key in lst:
    print(key, counts[key])

#prettier way of printing from dict
#for key in counts:
#    print(key, counts[key])

    