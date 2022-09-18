#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.

prompt = "Enter a number: "

avg = None
count = 0
total = 0
nr = 0
while True:
    try:
        nr = input(prompt)
        if nr == 'done':
            break
        count = count + 1
        total = total + int(nr)
        avg = total / count
    except:
        print('Invalid input')
        count = count - 1
        continue
print('Total:', total)
print('Count:', count)
print('Average:', avg)