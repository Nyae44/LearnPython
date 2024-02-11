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
        
        # We can assign attributes without specifying the parameters
        # When referring to class object attributes we can either use self or class name i.e self.pi or Circle.pi
        self.area = radius ** 2 * Circle.pi
      
      # Method   
    def get_circumference(self):
        return self.radius * pi * 2
    
my_circle = Circle(30)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)



# Inheritance and Polymorphism 

# Inheritance is the ability to form classes using classes that have already been defined 

# Advanatages of inheritance include:
#               - Ability to reuse code
#               - Reducing complexity of a program

class Animal():
    def __init__(self):
        print("Animal created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")
my_animal = Animal()
print(my_animal)
print(my_animal.eat())
print(my_animal.who_am_i())


class Cow(Animal):
    # Here Cow, inherits properties from the animal class 
    # An instance of the animal class is created when an instance of cow is created 
    
    def __init__(self):
        Animal.__init__(self)
        print("Cow created ")
    # We can overwrite methods from the inherited class 
    def who_am_i(self):
        print("I am a cow")
    # We are also able to add on to methods
    def moo(self):
        print("Mooo")
    # We can overwrite and add on to methods
    def eat(self):
        print("I am a Cow and I am eating")
        
my_cow = Cow()
print(my_cow)

# All methods that were available for animal are now available for Cow
# This is inheritance, I can now use methods that are common in classes
print(my_cow.eat())
print(my_cow.who_am_i())

# Add on to methods call

print(my_cow.moo())



# Polymorphism

# Refers to the way in which different object classes can have the same method name and the methods can be called from the same place 

class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + ' says meow!'
    
class Jackal():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + ' says wuuuu!'
        

        
niko = Cat('Bermuda')

rongo = Jackal('Rongo')

print(niko.speak())
print(rongo.speak())

# We can demonstrate polymorphism using a for loop
# Both Bermuda and Rongo share the same method name speak however they are of different types i.e __main__.Cat and __main__.Jackal

for pet in [niko,rongo]:
    print(type(pet))
    print(pet.speak())
    
    

# We can also demonstrate polymorphism through a function -> Is the most common way

def pet_speak(pet):
    print(pet.speak())
    
cat_pet_speak = pet_speak(niko)
print(cat_pet_speak)

jackal_pet_speak = pet_speak(rongo)
print(jackal_pet_speak)


# Another common way is to use abstract classes 
# An abstract class is a class that never expects to be instatiated -> no instance of the class is created 
# In the example below if you try to create an instance of the class bird you will get a NotImplemenetedError
# Because it expects a subclass to implement this method 

class Bird():
    
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Parrot(Bird):
    
    def speak(self):
        return self.name + "says quack quack!"
    
class Hen(Bird):
    
    def speak(self):
        return self.name + " says kookookoo!"
    
lambo = Parrot('Lambo')
print(lambo.speak())

rari = Hen('Rari')
print(rari.speak())



