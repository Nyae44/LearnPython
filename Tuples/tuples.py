# Tuples are very similar to lists however the key difference is that tuples are immutable
# Once an element is inside a tuple it cannot be reassigned 
# Tuples are denoted with a parethesis (1,2,3)

t = (1,2,3)
my_list = [1,2,3]
type(t) # Returns tuple
type(my_list) #returns List

# You can check the length of a tuple 
len(t)

print(len(t))

# A tuple can take different object types 
example_tuple = ('One', 3, 6.10)
# A tuple is ordered hence indexing and slicing can be done on a tuple
locate_one = example_tuple[0]
print(locate_one)

# Slicing

slice_it = example_tuple[1:]
print(slice_it)

# There are two built in methods for tuples that is the index method and the count method
recurrent = ('a', 'a', 'b', 'a', 'a')
# Count() method returns how many times an item appears in a tuple
print(recurrent.count('a'))

#Index() methods returns the index location of an element
# If an item appears more than once, it will only return the index of the very first time the item appears on the list
print(recurrent.index('a'))