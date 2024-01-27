# A list is an ordered sequence that can hold a variety of object types
# A list is denoted by square brackets and its elements are separated by commas
# A list is used where objects are retrieved by location hence can be indexed or sliced
my_list = [1,2,3]

# A list can hold different object types

my_updated_list = ['STRING', 100, 23.4]

# We use the len method when checking the length of the list i.e
print(len(my_list))
print(len(my_updated_list))
# Since list are ordered, we can perform indexing and slicing on them
my_list = ['One', 'Two', 'Three']
print(my_list[0])

print(my_list[0:3])

# We can also concatenate lists 
my_list = ['One', 'Two', 'Three']
another_list = ['Four', 'Five', 'Six']
update_list = my_list + another_list #saved 
print(update_list)

# Elements in a list are mutable
favorite_cars = ['Mazda CX5', 'Toyota Auris', 'Mercedes Benz C200',]
favorite_cars[1] = 'Urban Cruiser'
print(favorite_cars)

# Adding elements to a list -> We use the built in append() method which allows us to add a new item at the end of a list
favorite_cars.append('Toyota Mark X')
print(favorite_cars)

# Removing items from a list -> We use the pop method which allows us to remove an item from the end of a list
best_meals = ['Chapati Beans', 'Ugali Kales Eggs', 'Pilau', 'Spinach']
best_meals.pop()
print(best_meals)

# Lets implement a save action on a popped item so as to print it 
learning_flow = ['Python', 'JavaScript', 'React', 'Golang', 'Ruby']
popped_item = learning_flow.pop()
print(popped_item)
print(learning_flow)
# How to remove an item at a particular index -> You pass in the index as an argument to the pop method 
phone_brands = ['iPhone', 'Samsung', 'iTel', 'Xiaomi', 'Huawei']
phone_brands.pop(2)
print(phone_brands)

# How to sort a list using the sort method
reading_list = ['The art of war - Sun Tzu', 'Clean architecture - Robert C Martin' ]
reading_list.sort()
print(reading_list)

# Arranges the alpahbets in order
new_list = ['i', 'j', 'k','l', 'e', 'g', 'h', 'f', 'a', 'c', 'b', 'd']
new_list.sort()
print(new_list)

# Arranges the numbers in order 
num_list = [10, 6,5,8,4,1,3,2,9,7]
num_list.sort()
print(num_list)

# When using the sort method do not reassign it to a variable it would return a none type instead, you can
ranges = [4,5,6,8,2,1,3,7,9,10]
ranges.sort()
sorted_range = ranges
print(sorted_range)

# How to reverse a list using the built in reverse method

numbers = [1,2,3,4,5,6,7,8,9,10]
numbers.reverse()
print(numbers)