#Exercise 1: Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements

def chop(t):
    t[1:-1]
    
def middle(t):
    temp_list = t[1:-1]
    return temp_list

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t)
mod_list = middle(t)
print(mod_list)
print(chop(t))



