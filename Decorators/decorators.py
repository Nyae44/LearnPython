# Decorators allow you to add an extra functionality to an already existing function
# They use the @ operator and are placed on top of the original function 
# Syntax for decorators 

"""
@some_decorator
def simple_function():
    # Do simple stuff
    return something
"""


def func():
    return 1

def hello():
    return 'Hello!'

greet = hello

print(greet())

del hello
print(greet())

# Functions are objects that can be passed into other objects

# The greet and welcome functions are executed inside the hello function
# The scope of these functions is limited to the hello function,
# hence cannot be ex
def hello(name = 'Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is the greet() function inside hello()'
    
    
    def welcome():
        return '\t This is the welcome() function inside hello()'
    
    """
    print(greet())
    print(welcome())
    print('This is the end of the hello() function')
    """
    print('I am going to return a function')

    # Allows us to return a function which can be then assigned to a variable 
    if name[0].lower() == 'jose':
        return greet
    else:
        return welcome
print(hello())


my_new_func = hello('Daley')
print(my_new_func())

# Another example 

def cool():
    
    def super_cool():
        return 'I am very cool'
    return super_cool

some_func = cool()
print(some_func())

# Passing a function as an argument 

def hello():
    return 'Hi Jose'


def other(some_other_func):
    print('Other code runs here!')
    return some_other_func()

#The raw function is passed in then it is executed in the other function 
print(other(hello))


# Lets dive in Decorators 

def new_decorator(original_function):
    
    def wrap_func():
        print('Some extra code before the original function')
        original_function()
        print('Some extra code after the original function')
    return wrap_func()

def func_needs_decorator():
    print('I want to be decorated!!')
    
decorated_func = new_decorator(func_needs_decorator)


# Using the special syntax @ operator 
@new_decorator
def decorate_this_one():
    print('Oh! I love decorations')