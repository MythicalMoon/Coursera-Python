#Exercise 2: Write another program that prompts for a list of numbers
#as above and at the end prints out both the maximum and minimum of
#the numbers instead of the average.
prompt = "Enter a number: "

avg = None
largest = None
smalest = None
count = 0
total = 0
nr = 0
values = []
while True:
    try:
        nr = input(prompt)
        if str(nr) == 'done':
            break
        values.append(int(nr))
        count = count + 1
        total = total + int(nr)
        avg = total / count
    except:
        print('Invalid input')
        count = count - 1
        continue
    print(values)
    for i in values:
        if largest is None or i > largest:
            largest = i
        if smalest is None or i < smalest:
            smalest = i            
print('Total:', total)
print('Count:', count)
print('Average:', avg)
print('Largest:', largest)
print('smalest:', smalest)