# List comprehensions are a unique way of quickly creating a list in Python
# If you find yourself using a for loop along with .append() to create a list, comprehensions are a good alternative 


mystring = 'Hello'
# To print every character as a list;
mylist = []
for letter in mystring:
    mylist.append(letter) 
#    print(mylist)


# Using list comprehensions
# The syntax is:
"""
list_name = [element for element in iterable]
iterable -> Be it a string, list
"""

mynewlist = [letter for letter in mystring]
print(mynewlist)
# The variable name in the list comprehension syntax can be any word of your choice
makelist = [x for x in 'Word']
print(makelist)

# Using the built range function with list comprehension to create a list

mynumbers = [num for num in range(0,11)] # Creates a list from 0 - 10
print(mynumbers)

# You can also square numbers using list comprehension

square_numbers = [num**2 for num in range(0,21)] # num**2 is the same as append()
print(square_numbers)

# Another way to square 

for square in range(0,10):
    print(square**2)

# You can also add an if statement 
# To print the even numbers 

even_numbers = [x for x in range(0,11) if x % 2 == 0]
print(even_numbers)

# We can square the even numbers 
square_even_numbers = [x**2 for x in range(0,11)if x % 2 == 0]
print(square_even_numbers)

# To perform complex arithmetic 

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp + 32)for temp in celcius]
print(fahrenheit)

# Let break it down as a for loop to get the connection behind the logic 

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp +32))
    print(fahrenheit)

# Using if else statement with list comprehension
# It can be used but it is essential that we maintain readablity in code

results = [x if x % 2 == 0 else 'ODD' for x in range(0,10)] 
print(results)

# You can also do nested loops in a list comprehension 

# Lets take a look at the implementation of a nested loop 

mynestedlist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mynestedlist.append(x*y)
        print(mynestedlist)

# We can do a nested loop in list comprehension at the expense of readability

nestlist = [x*y for x in [2,4,6] for y in [1, 10, 1000]]
print(nestlist)
        