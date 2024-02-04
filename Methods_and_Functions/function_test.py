import re


def myfunc(name):
    print('Hello {}'.format(name))

testfunc = myfunc('Nyae')

"""
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd¶

"""
def lesser_of_two_evens(a,b):
    if a % 2==0 and b % 2 ==0:
        if a<b:
            return a
        return b
    elif a % 2 == 1 or b % 2 == 1:
        if a > b:
            return a
        return b
    
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
    index = text.lower().split()
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
# One line interpretation -> return (num1 + num2) == 20 or num1 == 20 or num2 == 20
make_twenty_check = make_twenty(21,3)
print(make_twenty_check)

"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""
def old_macdonald(name):
    first_letter = name[0]
    middle_letter = name[1:3]
    fourth_letter = name[3]
    rest_of_letters = name[3:]

    return first_letter.upper() + middle_letter + fourth_letter.upper() + rest_of_letters

string_manipulation = old_macdonald('macdonald')
print(string_manipulation)

# We could also use the capitalize method
"""
firsthalf = name[:3]
secondhalf = name[3:]
return firsthalf.capitalize() + secondhalf.capitalize()
"""

"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

"""
def master_yoda(text):
    split_text = text.split()
    reverse_text = split_text[::-1]
    # For it to return a string we have to use .join() list method
    return_as_string = ' '.join(reverse_text)
    return return_as_string

result_master_yoda = master_yoda('I am home')
result_master_yoda_2 = master_yoda('We are ready')
print(result_master_yoda)
print(result_master_yoda_2)

"""
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
# Absolute value check
"""
def almost_there(n):
    return (abs(100-n)<=10) or (abs(200-n)<=10)

result_almost_there = almost_there(150)
result_almost_there_2 = almost_there(209)
result_almost_there_3 = almost_there(104)
print(result_almost_there)
print(result_almost_there_2)
print(result_almost_there_3)

"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""
def has_33(num):
    for i in range(0, len(num)-1):
        if num[i] ==3 and num[i+1] == 3:
            return True
    return False

result_has_33 = has_33([1,1,3,3])
result_has_33_2 = has_33([1,3,1,3])
print(result_has_33)
print(result_has_33_2)

"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(text):
    modified_text = ""
    for char in text:
        modified_text += char *3 
    return modified_text

result_paper_doll = paper_doll('Hello')
result_paper_doll_1 = paper_doll('Mississippi')
print(result_paper_doll)
print(result_paper_doll_1)

"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""
def blackjack(a,b,c):
    """
    blackjack(a,b,c)
    
    This function takes three integers between 1 and 11 as input parameters.
    It calculates the sum of the three integers and checks if the sum is less than or equal to 21.
    If the sum is less than or equal to 21, it returns the sum.
    If the sum exceeds 21 and there is an eleven (11) among the integers, it reduces the total sum by 10 and returns the adjusted sum.
    If the sum (even after adjustment) exceeds 21, it returns the string 'BUST'.
    """
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
        return sum([a,b,c]) - 10
    return "BUST"

result_black_jack = blackjack(5,6,7)
result_black_jack_1 = blackjack(9,9,9)
result_black_jack_2 = blackjack(9,9,11)
print(result_black_jack)
print(result_black_jack_1)
print(result_black_jack_2)

"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14

"""
def sommer_69(arr):
    total_sum = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total_sum += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total_sum


result_sommer_69 = sommer_69([1,3,5])
result_sommer_69_1 = sommer_69([4,5,6,7,8,9])
result_sommer_69_2 = sommer_69([2,1,6,9,11])
print(result_almost_there)
print(result_almost_there_2)
print(result_almost_there_3)

"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False

"""
def spy_game(nums):
    code = [0,0,7, 'x']
    # [0,7,'x']
    # [7, 'x']
    # ['x'] length == 1
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return len(code) == 1

result_spy_game = spy_game([1,2,4,0,0,7,5])
print(result_spy_game)
result_spy_game_1 = spy_game([1,0,2,4,0,5,7])
print(result_spy_game_1)
result_spy_game_2 = spy_game([1,7,2,0,4,5,0])
print(result_spy_game_2)

"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
"""
def count_primes(num):
    # check 0 or 1 input
    if num < 0:
        return 0
    # 2 or greater
    # store our prime numbers
    primes = [2]
    # Counter that goes upto the input num
    x = 3

    # X is going through every number upto input number 
    while x <= num:
        # check if x is prime
        for y in range(3,x,2):
            if x % y == 0:
                x += 2
                break
        # For else 
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


result_count_primes = count_primes(100)
print(result_count_primes)