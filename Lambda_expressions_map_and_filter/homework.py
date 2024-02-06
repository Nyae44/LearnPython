"""
Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as
4/3π𝑟3
"""



def vol(rad):
    volume = (4/3) * (3.142) * rad**3
    return volume
ans_vol = vol(2)
print(ans_vol)

"""
Write a function that checks whether a number is in a given range (inclusive of high and low)

"""
def ran_check(num,low,high):
   if num in range(low, high +1):
       return f'{num} is in range {low}, {high}'
   return 'Dogo wacha bangi'
   
ans_ran_check = ran_check(32,1,10)
print(ans_ran_check)

"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output : 
No. of Upper case characters : 4
No. of Lower case Characters : 33
HINT: Two string methods that might prove useful: .isupper() and .islower()

If you feel ambitious, explore the Collections module to solve this problem!
"""
def up_low(s):
    uppercase = 0
    lowercase = 0
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'Original string is {s}')
    print(f'Uppercase count {uppercase}')
    print(f'Lowercase count {lowercase}')

ans_up_low= up_low('Hey Sally, I love you so much')
print(ans_up_low)

# Using dictionaries
def capitalize(t):
    d = {'upper': 0, 'lower': 0}
    for char in t:
        if char.isupper:
            d['upper'] += 1
        elif char.islower:
            d['lower'] += 1
        else:
            pass
    print(f'Original string is {t}')
    print(f'Upper count: {d["upper"]}')
    print(f'Lower count: {d["lower"]}')
"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
"""

def unique_list(lst):
    return set(lst)
ans_unique_list = unique_list([1,1,1,2,2,3,3,3,4,4,5,5,6,6])
print(ans_unique_list)

"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
"""
def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total

"""
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: 
You may want to check out the .replace() method in a string to help out with dealing with spaces.
 Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
"""
def palindrome(s):
    # Remove the spaces in a string
    s = s.replace(' ','')
    # Make s in one casing 
    s = s.lower()

    # Check if s == reversed version of the string 
    if s == s[::-1]:
        return True
    return f'{s} is not a palindrome'

ans_palindrome = palindrome('Mom')
print(ans_palindrome)

"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"
Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons
"""

import string
def ispangram(str1, alphabet =string.ascii_lowercase):
    # Create a set of alphabet
    alphaset = set(alphabet)

    # Remove any spaces from the input 
    str1 = str1.replace(' ', '')
    # Convert into all lowercase
    str1 = str1.lower()
    # Grab all unique letters from the string
    unique_letters_set = set(str1)
    # alphabet set == string set
    if alphaset == unique_letters_set:
        return True
    return False

ans_ispangram = ispangram("The quick brown fox jumps over the lazy dog")
print(ans_ispangram)

