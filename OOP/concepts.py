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

class Dog():
    def __init__(self, breed, name, spots):
        # Attributes 
        # We take in the argument 
        # Assign it using self.attribute
        self.breed = breed
        self.name = name
        
        # Expect boolean True/False
        self.spots = spots
        
my_dog = Dog('Rottweiler', 'Jiji', True)
print(type(my_dog))
print(my_dog.breed)