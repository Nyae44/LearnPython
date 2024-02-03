def myfunc(name):
    print('Hello {}'.format(name))

testfunc = myfunc('Nyae')

"""
Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

Remember, don't run the function, simply provide the definition.

To give an idea what the function would look like when tested:

    myfunc('Anthropomorphism')
    # Output: 'aNtHrOpOmOrPhIsM'

Added note: this exercise requires that the function return a string. Print statements will not work here.

"""
# Enumarate function allows us to iterate through a sequnce and keep track of the index of every character

def stringfunc(word):
    modified_word = ""
    for i, char in enumerate(word):
        if i % 2 == 0:
            modified_word += char.upper()
        else:
            modified_word += char.lower()
    return modified_word

test_this = stringfunc('fantastic')
print(test_this)


"""
Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶

"""

def check_size(a,b):
    if a and b % 2 == 0:
        if a < b:
            return a
        else:
            pass
    elif a and b % 2 == 1:
        if a > b:
            return a
        else:
            return b
    else:
        pass

my_result = check_size(2,5)
print(my_result)

"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
"""
def animal_crackers(text):
    index = text.split()
    if index[0][0] == index[1][0]:
        return True
    return False
  
animal_check = animal_crackers('Levelheaded Llama')
print(animal_check)

"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
"""
def make_twenty(num1, num2):
    if num1 + num2 == 20:
        return True
    elif num1 == 20:
        return True
    elif num2 == 20:
        return True
    return False
make_twenty_check = make_twenty(21,3)
print(make_twenty_check)

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""
def old_macdonald(name):
    modified_name = " "
    if len(name) < 4:
        return "Name is less than 4 characters"
    for i,char in enumerate(name):
        if i == 0 or i == 3:
             modified_name += char.upper()
      
    return modified_name

result_old_macdonald = old_macdonald('Daley')
print(result_old_macdonald)