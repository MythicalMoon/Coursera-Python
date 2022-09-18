#Exercise 6: Rewrite your pay computation with time-and-a-half for over-
#time and create a function called computepay which takes two parameters
#(hours and rate).

def computepay(hours,rate):
    if hours < 40:
        pay = float(hours) * float(rate)
    else:
        pay = float(hours) * ( float(rate) * 1.5 )
    print("Pay:", pay)
    
try:
    hours = float(input("Input your weekly hours: "))
    rate = float(input('Input your rate: '))
except:
    print('Enter a valid number')

computepay(hours,rate)