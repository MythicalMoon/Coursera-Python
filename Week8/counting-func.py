#Exercise 3: Encapsulate this code in a function named count, and gen-
#eralize it so that it accepts the string and the letter as arguments

def count12(word, s_letter):
    a = 0
    for letter in word:
        if letter == s_letter:
            a = a + 1 
    print('The word:', word, 'contains', a, letter + "'s")
        

word = "sausage"
s_letter = str(input('provide a letter'))
count12(word, s_letter)
