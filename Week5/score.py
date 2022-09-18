#Exercise 3: Write a program to prompt for a score between 0.0 and
#1.0. If the score is out of range, print an error message. If the score is
#between 0.0 and 1.0, print a grade using the following table

prompt = "enter a value between 0.0 and 1.0: "
try:
    score = float(input(prompt))
except:
    print('Enter a valid number!')

if score < 0.0 or score > 1.0:
    print('Out of bounds!')
else:
    if 0.9 <= score <= 1.0:
        print('A')
    if 0.8 <= score < 0.9:
        print('B')
    if 0.7 <= score < 0.8:
        print('C')
    if 0.6 <= score < 0.7:
        print('D')
    if score < 0.6:
        print('F')