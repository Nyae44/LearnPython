# Are unordered collections of unique elements 
# There can only be one representative of the same object
myset = set()

# To add an  object to the set we can call the add method on myset variable
myset.add(1)
print(myset)
myset.add(2)
print(myset)

# If add the number 2 a second time it will only show the value 2 one time
myset.add(2)
print(myset)
# Casting a list to set to only get the unique values 
mylist = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,]
print(set(mylist))