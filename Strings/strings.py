#Indexing
name = "Daley Nyae"
print(name[1])
"""
- Strings are an ordered sequence of characters
- We can use indexing and slicing to grab subsecions of the string
- These actions use [] and a number index to indicate the positions you wish to grab
character: h e l l o
    index: 0 1 2 3 4
re index:0 -4 -3 -2 -1
"""
#Slicing 
mystring = "Hello World"
print(mystring[:3])
print(mystring[8])
teststring = "abcdefghijk"
print(teststring[3:6])
print(teststring[1:3])
print(teststring[3:9])
#Step size jump
print(teststring[::3]) # step size of 3 prints adgj
print(teststring[::1]) # prints characters as they are
print(teststring[2:7:2]) #can be used in combination of start and stop
#Reverse a string
print(teststring[::-1])
#Is Mom a palindrome? lets try reversing it
parent = "mom"
print(parent[::-1])

"""
- A step size of 1 prints characters as they appear
- Allows us to grab subsections of multiple characters
- it has the syntax[start:stop:step]
- Start -> numerical index for slice start
- Stop  -> is the index you will go upto but not included
- Step  -> is the size of the jump you take
"""
# NOTE: Spaces are identified as characters 


#String properties and methods
    #Immutability of strings
first_name = "Daley"
# first_name[0] = "N" # You get an object does not support item assignment error
print(first_name) 
change_letters = first_name[1:]
print("N"+ change_letters) # We performed string concatenation

# Multiple concatenations
letter = "D"
multiple = letter *10
print(multiple)

# String methods
x = "Hello Mwele"
x.upper()
print(x.upper())

x = x.split
print(x)

#split method
statement = "This is a string"
print(statement.split()) # Splits the string in a list
splitter = statement
print(splitter.split("i")) # Splits wherever it finds an i

# String interpolation -> Injecting variables into strings
"""
There are two main methods 
.format()
f-strings
"""
print("This is a string{}".format(" INSERTED"))
print("The {} {} {}".format("dog", "bit", "me")) # The strings take the order given 
#To change the order we use indexing  i.e
print("The {1} {0} {2}".format("brown", "quick", "fox")) 
# We could call one element of the same index repeatedly

print("The {2} {2} {2}".format("brown", "quick", "fox")) 
# We could also assign the words keywords

print("The {q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))

# Float formatting -> Used to format the width and precision when working with floating point numbers 
# Takes the format {value:width.precision f}
result = 100/777
print(result) # Prints the whole floating point number
print(" The result is {r:1.3f}".format(r = result)) # Prints the result with a precision of 3 decimal places
# If you tinker around with the width you end up adding more whitespace 

# f-strings method 
your_name = "Jose"
print(f"Your name is {your_name}")

patient_name = "Charlene"
age = 25
print(f" {patient_name} is {age} years old")