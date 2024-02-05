# Scope -> Enables Python understand the variables in a given context and scope follows particular rules LEGB
# When you declare variables inside a function, the variables are only available for that function
"""
L : Local -> Names assigned in any way within a function (def or lambda) and not declared global in that function.
E : Enclosing function locals -> Names in the local scope of any and all enclosing functions(def or lambda) from inner to outer 
G : Global module -> Names assigned at the top level of a module file or declared global in a def within the file
B : Built in (Python) -> Names preassigned in the built in names module 
"""
x = 25 

def printer():
    x = 50 
    return 50

# This print call will reference the first value assigned to variable x 
print(x)

# This print call will refer to the second value assigned to x inside the printer function
print(printer())

# Local variable example
lambda num : num ** 2 # num is an example of a local variable within a lambda expression

# An example of Enclosing function locals -> To illustrate this we create a function and put another function inside the function
# Global -> is defined by no indentation
name = 'THIS IS A GLOBAL STRING'

def greet():
    # Enclosing
    name = 'Sammy'

    def Hello():
        #Local
        name = 'Daley'
        print('Hello' + name)
    Hello()
greet()

# This function returns Hello Sammy since inside the greet function name is assigned to 'Sammy' internally


t = 50 

def func(x):
    global t
    print(f'T is {t}')
    # Local reassignment
    t = 'New value'
    print(f'I just locally reassigned t to {t}')
func(t)

