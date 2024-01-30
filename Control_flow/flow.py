# We often want a certain code to execute when a particular condition is met
# For example, if my dog is hungry(some condition) then i will feed the dog(some action)
# There are three main keywords in control flow -> if, elif and else
# Control flow makes use of colons and indentation(whitespaces)
# This indentation system allows Python code to be easily readable and very quick to prototype
"""
    if some_condition:
        # execute some code
    elif:
        # do something different
    else:
        # do something else 

"""
# Starter example 

if True:
    print('True')

# Realistic example 
    hungry = False  # switch to False to get the difference
    if hungry:
        print('Feed Me')
    else:
        print('Oh i\'m full')

# Example with multiple branches 
# The indentation is executed as part of the code 
loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!')
elif loc == 'Store':
    print('Welcome to the store')
else:
    print('I do not know much')

# Exmaple to illustrate indentation

name = 'Jose'
# note the indentation
if name == 'Madison':
    print('Hello, Madison!')
elif name == 'Daley':
    print('Hello, Daley!')
else:
    print('What is your name?')