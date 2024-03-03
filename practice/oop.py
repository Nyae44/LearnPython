# Object oriented programming
# pretty much everything that we work on in Python is an object  
x = 1 
print(type("Hello")) # returns <class 'str'> which means this is an object of class string
print(type(x)) # returns <class 'int'> -> is an object of class int 

def hello():
    print("hello")
    
print(type(hello)) # returns <class 'function'> -> is an object of class function


# methods
string = 'hello'
print(string.upper()) # .upper() is the method

# classes 

# The following example is a template example to illustrate on classes

class Dog:
    def bark(self):
        print('Woof! Woof!')
    def eat(self):
        print("Dog is eating lasgne")
# d will be an object of type Dog
# Here we are creating an instance of the Dog class and assigning it to a variable d
d = Dog()
print(type(d)) # returns <class '__main__'.Dog> -> __main__ is module in which this class was defined

# By default the module run is called the main module 

# Using a method on an instance of the dog class
d.bark()
d.eat()
