#Exercise 6: Rewrite the program that prompts the user for a list of
#numbers and prints out the maximum and minimum of the numbers at
#the end when the user enters “done”. Write the program to store the
#numbers the user enters in a list and use the max() and min() functions to
#compute the maximum and minimum numbers after the loop completes

num_list = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = int(inp)
    num_list = num_list + [value]
      
print(num_list)
print(f"max number: {max(num_list)}")
print(f"min number: {min(num_list)}")
    
    
