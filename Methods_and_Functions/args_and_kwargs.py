# *args - Arguments 
# **kwargs - Keyword arguments 

# a,b are examples of positional arguments, that is, 4 is assigned to a since its in the first position and 6 to be because its in the second position
# Notice that when we want to work with multi-positional arguments as a sum we have to pass them as a tuple
def myfunc(a,b):
    return sum((a,b)) * 0.05
result = myfunc(4,6)
print(result)


# *args -> allows a function to take an arbitrary/variable number of arguments
#  *args is treated as a tuple of parameters 

def examplefunc(*args):
    return sum(args) * 0.05

return_result = examplefunc(10,20) # Can take a variable number of arguments and parameters

# **kwargs - Allows a function to take an arbitrary/variable number of keyworded arguments and parameters
# **Kwargs builds a dictionary with key value pairs 

def keyword_func(**kwargs):
    print(kwargs) # To check the kwargs data type
    if 'fruit' in kwargs:
        print('My fruit of choice is {} and {} as vegetables'.format(kwargs['fruit'], kwargs['veggies']))
    else:
        print('I did\'nt find any fruit here')
    
result_func = keyword_func(fruit ='Watermelon', veggies = 'Spinach')
print(result_func)

# In Python we can use both a combination of args and kwargs 
# Whenever we are using both args and kwargs, we to do so in the order *args first then **kwargs
def samplefunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))

sample_result = samplefunc(10,20,30, food = 'Eggs', fruit = 'Oranges', vegetables = 'Spinach')
print(sample_result)