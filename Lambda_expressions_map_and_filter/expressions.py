# Lambda expressions, map and filter functions 


# Map -> Applies a function to every item in an iterable
# When passing a function to the map function we do not add the execution parenthesis since map will self execute the function



def square(num):
    return num**2

mylist= [2,4,5,6,7,8,10]

for item in map(square,mylist):
    print(item)

# If you want to return the items as a list 

newlist = [3,5,6,7,8,88,9,999]

sqaure_nums = list(map(square,newlist))
print(sqaure_nums)

# A function that works with strings 
def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'EVEN'
    return mystring[0]

names = ['Daley', 'Nyae', 'Tinga', 'Python', 'Guido', 'Jedi', 'Knight']
for item in map(splicer,names):
    print(item)

spliced = list(map(splicer,names))
print(spliced)

# Filter function -> Filters elements based on the function's condition 
def check_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for number in filter(check_even,numbers):
    print(number)

# If we want to return the filtered numbers as a list

filtered_numbers = list(filter(check_even, numbers))
print(filtered_numbers)

# Lambda Expressions -> Is also known as an anonymous function and is only used once in a program hence it is not given a name
# nor does it take the function definition syntax
# Instead of a name and the keyword def, it takes the keyword lambda
# The syntax for a lambda expression is as follows 
# lambda num : num ** 2 -> the parameter num is used for illustration purposes
# We will break down a function until it becomes a lambda expression then finally explain lambda expressions

def sqaure_this(num):
    result = num ** 2
    return result
# We will turn the above function into a lambda expression step by step
def modified_square_this(num):
    return num ** 2
# Make it in one line 

def mod_square_this(num): return num ** 2

# Whoa, a lambda expression

sqaure = lambda num : num ** 2
test_this = sqaure(5)
print(test_this)

# Labda Expressions are commonly used in conjuction with other functions such as map and filter
test_list = [2,4,6,7,8,9,10]
test_list_squared = list(map(lambda num:num ** 2, test_list)) # Applies lambda function to list and returns result as list
print(test_list_squared)

# Lambda with filter
filter_even = [1,2,3,4,5,6,7,8,9,10]
filtered_list = list(filter(lambda num : num % 2 == 0, filter_even))
print(filtered_list)

# Lambda expressions can be used for string manipulation say you want to grab the first character in a list

my_name = ['Daley', 'Nyae', 'Tinga']
manipulated_list = list(map(lambda name : name[0], my_name))
print(manipulated_list)

# Reverse the my_name

reversed_list = list(map(lambda name: name[::-1], my_name))
print(reversed_list)