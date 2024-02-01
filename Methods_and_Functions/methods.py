# Methods are functions built into objects

mylist = [1,2,3,4,5]
# Adds an item at the end of the list
mylist.append(6)
print(mylist)

# Removes an item at the end of the list
mylist.pop()
print(mylist)

# How to discover methods in your own add dot to the variable name
# mylist. lists all in built methods when working with list
# Using the built in help function is another way to understand what a particular function does i.e
# Another option is to view the python documentation

print(help(mylist.clear))
mylist.extend([6,7,8])
print(mylist)
print(mylist.index())
 