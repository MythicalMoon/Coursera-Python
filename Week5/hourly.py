# Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.
try:
    hours = float(input("Input your weekly hours: "))
    rate = float(input('Input your rate: '))
except:
    print('Enter a valid number')

if hours < 40:
    pay = float(hours) * float(rate)
else:
    pay = float(hours) * ( float(rate) * 1.5 )
print(pay)