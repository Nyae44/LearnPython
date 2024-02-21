'''
Problem 1
Create a generator that generates the squares of numbers up to some number N.
'''

def gen_squares(N):
    for x in range(N):
        yield x **2 
        

for x in gen_squares(10):
    print(x)
    
"""
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs).
Note: Use the random library. For example:
"""
from random import randint
import random
randint(1,10)


def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)
        
for num in rand_num(1,10,12):
    print(num)
    
"""
Problem 3
Use the iter() function to convert the string below into an iterator:
"""

s = 'hello'
s = iter(s)
print(next(s))

"""
Problem 4
Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.

answer:
if the output has the capability of taking up more memory than the intended
"""
