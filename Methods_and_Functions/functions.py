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