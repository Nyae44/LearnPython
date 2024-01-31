# For loop
# Many objects in Python are iterable, meaning you can go through them
# You can iterate over a list, characters in a string, keys in a dictionary
# We use for loops to execute a block of code for every iteration
# Syntax of a for loop
"""
my_iterable = [1,2,3]

for item_name in my_iterable:
    print(item_name)

Output:
1
2
3

"""

my_list = [1,2,3,4,5,6,7,8,9,10]

# The variable name can be any name of choice, the choice of num is influenced my the integer objects in my_list
for num in my_list:
    print(num)

# We add control flow to print out the list of even numbers 

for number in my_list:
    # Check for even
    if number % 2 == 0:
        print(f'Even number: {number}')
    else:
        print(f'Odd number: {number}')
# Square number in a list
"""
new = []
for square in my_list:
    new.append(square**2)
    print(new)

"""
list_sum = 0
for number in my_list:
    list_sum = list_sum + number
    # If we only want to see the last result we indent outside of the for loop
print(list_sum)

# Iterating through strings 

my_string = 'Hello World'
for letter in my_string:
    print(letter) 

# Iterating through tuples 

tup = (1,2,3)
for item in tup:
    print(item)

# Tuple unpacking

mylist =[(1,2), (3,4),(5,6),(7,8)]
print(len(mylist))
for item in mylist:
    print(item)
    
# Tuple unpacking -> We extract the values in of the tuple into a single variable
# The parethesis is optional you could do 
for (a,b) in mylist:
    print(a)
    print(b)
# More Examples 

my_tuple_list = [(1,2,3), (4,5,6)]
for item in my_tuple_list:
    print(item)
for (a,b,c) in my_tuple_list:
    print(a)
    print(b)
    print(c)

# Iterating through a dictionary
# By default when you iterate through a dictionary you iterate through the keys 
# When you use .items() you get back the key and value
d = {'K1':1, 'K2':2, 'K3':3}
for item in d.items():
    print(item)

for key,values in d.items():
    print(values)

for values in d.values():
    print(values)