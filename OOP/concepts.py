#  OOP -> Allows programmers to create objects that have methods and attributes
# Enables us to create code that is repeatable and organized 

"""
class NameOfClass():
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2 
    def some_method(self):
        # Perform some action
        print(self.param1)
"""

from math import pi


class Dog():
    # Class object attribute 
    # Is the same for any instance of a  class
    # We use species since class is a keyword in python
    species = 'mammal'
    def __init__(self, breed, name):
        # Attributes 
        # We take in the argument 
        # Assign it using self.attribute
        self.breed = breed
        self.name = name
        
        #
    # Methods are operations/ actions 
    # Methods can take outside arguments 
    def bark(self, age):  #self connects bark to the actual object
        print('Wooof my name is {} aged {}'.format(self.name, age))
        
        
my_dog = Dog('Rottweiler', 'Jiji')
print(type(my_dog))
print(my_dog.breed)
print(my_dog.bark(10))


class Circle():
    # Class object attribute 
    pi = 3.14 
    
    def __init__(self, radius = 1):
        self.radius = radius
      
      # Method   
    def circumferrence(self):
        return self.radius * pi * 2