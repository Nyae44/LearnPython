# Functions allow us to create blocks of code that can be executed many times without needing to rewrite the entire block of code 
# To create a function we use the keyword def
# Creating a function in Python requires a specific syntax, including the def keyword, correct indentation and proper structure
# Here is an overview of a function structure in Python
# The def keyword tells python that this is a function
# The name of the function uses snake casing i.e lowercase and underscores between words
# The parenthesis come at the end of name of the function and here we can pass in arguments or parameters to the function
# The colon indicates an upcoming indented block 
# Followed by a Docstring -> a multi-line comment which explains what a function is supposed to do 
# Everything inside a function is indented 
# The you write the code inside the function

def name_of_function():
    """
    Docstring - Multiline comment that explains what a function does 
    """
    print('Hello')

# Function can then be called or executed as follows
name_of_function()

# Functions can accept arguments to be passed by the user 

def user_name(name):
    """
    function to print the user's name as provided by the user 

    """
    print("Hello " + name)

user_name('Jose')

# We use the return keyword to print out the output of a function instead of printing it out 
# Return allows us to assign the output of a function to a new varible 

def add_function(num1, num2):
    return num1 + num2

result = add_function(3,5)
print(result)

# A function can take in input parameter/ arrguments 

def say_hello(name):
    print(f'Hello {name}')
say_hello('Daley')

# We could use a default value incase user input is not provided

def say_goodbye(name = 'Default'):
    print(f'Goodbye {name}')
say_goodbye() # Prints Goodbye default since the details are not provided

# When using functions we are going to use return keyword instead of printing out stuff inside the function
# I've added default numbers in case user forgets to pass the number arguments 
def add_num(num1 = 1,num2 = 1):
    # Return allows us to save to a variable
    return num1 + num2
result = add_num(3, 4)
print(result)

# Difference between print and return 
# Print -> Will not return anything to be saved 
# Return -> Can actually be saved  to a variable
def print_result(a,b):
    print(a+b)
print_result(3,5)

def return_result(a,b):
    return a + b
result = return_result(3,8)
print(result)

# Make sure to check the data type when dealing with user input i.e
def sum_numbers(num1, num2):
    return num1 + num2
result = sum_numbers('10','20') 
print(result) # Prints out '1020' since the plus sign concatenates the string
# TODO: Address this issue!

# Functions with logic
def even_check(number):
    result = number % 2 == 0 # This assignment is for knowledge purpose you could directly return number % 2 ==0  its just the same thing
    return result
check_number = even_check(39)
print(check_number)

# A function that returns True if any number is even inside a list
# Think of return as essentially breaking out of the function
# It is wrong to call another return statement after an initial one within the same indentation
# Instead break out of the indentation and return in line with the for loop indentation
def check_even_list(numlist):
    for number in numlist:
        if number % 2 == 0:
            return True
        else:
            pass
    return False
list_checker = check_even_list([2,4,6])
print(list_checker)

# Edgecases
first_number_even = check_even_list([2,1,1,1,1,1])
print(first_number_even)
last_number_even = check_even_list([1,1,1,1,12])
print(last_number_even)

# Return even numbers in a list
def return_even_numbers_list(numberlist):
    even_numbers = []
    for number in numberlist:
        if number % 2 == 0:
            return even_numbers.append(number)
        else:
            pass
    return even_numbers

# Tuple unpacking with python functions 

# Recall

stock_prices = [('Apple', 200), ('Google', 400), ('Microsoft', 100)]
# We could print all items as 
for item in stock_prices:
    print(item)

# We could do tuple unpacking 
for company, stock_price in stock_prices:
    print(company)
    print(stock_price)

# Report a 10% increase
for company, stock_price in stock_prices:
    print(stock_price + (0.1 * stock_price))

# We could do tuple unpacking with Python functions 
work_hours = [('Daley', 100), ('Billy', 2000),('Audrey', 150), ('James', 250)]
# We want to get the employee that worked for the most hours 

def check_employee(work_hours):
    # Placeholder varible -> Is a variable with which we will assign a varible later 
    current_max = 0
    employee_of_the_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass

    # Return
    return (employee_of_the_month, current_max)

        
check_results = check_employee(work_hours)
print(check_results)

# We could also print them as seperate varibales

name, hours = check_employee(work_hours)
print(name)
print(hours)

# Interactions between functions

example = [1,2,3,4,5,6,7,8,9]

# If you want to randomly shuffle the list we import shuffle from the random library
from random import shuffle
shuffle(example)
print(example)

# We create a guessing game to illustrate how functions interact with other functions 2
# Lets create our own function that can create the list and shuffle it 
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

result = shuffle_list(example)
print(result)

# User has to guess the position of 'O'
my_list = ['','O','']

# Create a user guess function to illustrate this 
def player_guess():
    guess = ''
   

    while guess not in ['0','1','2']:
         guess = input('Pick a number, 0,1 or 2  ')
   
    return int(guess)


# myindex = player_guess()
# print(myindex)

# We create another function to check whether the guess is correct 

def check_guess(my_list,guess):
    if my_list[guess] == 'O':
        print('Correct!')
    else:
        print('Wrong guess!')
        print(my_list)


# Order of functions

# Initial list
my_list = ['','O','']
# Shuffle list
mixeduplist = shuffle_list(my_list)
# User guess
guess = player_guess()
# Check guess 
check_guess(mixeduplist,guess)