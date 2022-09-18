#Exercise 7: Rewrite the grade program from the previous chapter using
#a function called computegrade that takes a score as its parameter and
#returns a grade as a string.

def computegrade(score):
    if score < 0.0 or score > 1.0:
        print('Out of bounds!')
    else:
        if 0.9 <= score <= 1.0:
            grade = 'A'
        if 0.8 <= score < 0.9:
            grade = 'B'
        if 0.7 <= score < 0.8:
            grade = 'C'
        if 0.6 <= score < 0.7:
            grade = 'D'
        if score < 0.6:
            grade = 'F'
        return str(grade)
        
prompt = "enter a value between 0.0 and 1.0: "
try:
    score = float(input(prompt))
except:
    print('Enter a valid number!')
    
grade = computegrade(score)
print(grade)
print(type(grade))