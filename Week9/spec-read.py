#Exercise 2: Write a program to prompt for a file name, and then read
#through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:”
#pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence
#90 CHAPTER 7. FILES
#values from these lines. When you reach the end of the file, print out
#the average spam confidenc
count = 0
sum_extract = 0
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
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
        