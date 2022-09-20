#easter egg for "na na boo boo"

count = 0
sum_extract = 0
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("WAAAAA!")
    print('file with the name:', fname, "doesn't exist!")
    exit()

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        atpos = line.find(':')
        extract = float(line[atpos+1:])
        count = count + 1
        sum_extract = sum_extract + float(line[atpos+1:])
avg_extract = float(sum_extract) / count
print('Average spam confidence: %g' % avg_extract)
        