# Dictionaries are unordered mappings for strings
# Are used where objects are retrieved by Key name
# Dictionaries are unordered hence they cannot be sorted 
# Dictionaries are denoted by curly braces and are seperated by colons
# Dictionaries syntax {'Key1':'value1', 'Key2':'value2'}
my_dict = {'book1':'English', 'book2': 'Mathematics'}
print(my_dict)

#To get values from dictionaries we pass the key inside square brackets ['key']
book_value = my_dict['book1']
print(book_value)

# Real world example to check item prices 
price_lookup = {'apple': 100, 'bananas':20, 'Mango':20, 'Oranges':50, 'Pineapples':100}
whats_the_price = price_lookup['apple']
print(whats_the_price)
# Dictionaries are flexible on the data that they can hold i.e the can also hold lists and other dictionaries 
d = {'key1': 'Primary Key', 'key2': [1,2,3,4,5], 'key3': {'Id':36721020, 'Phone Number': +254742660902, 'Age': 24}}
key1 = d['key1']
print(key1)
key2 = d['key2']
print(key2)
key3 = d['key3']
print(key3)
# To access elements of the list nested inside the dictionary
access_list = d['key2'][1]
print(access_list)
# To access the elements of the dictionary nested inside the dictionary you can stack the key call of what you want to access
access = d['key3']['Id']
print(access)

# Test change an element in list nested in a dictionary to uppercase
alphabets = {'Key1': ['a', 'b' , 'c']}
make = alphabets['Key1'][2].upper()
print(make)

# Add an element to a dictionary
reading_list = {'book1': 'Clean Architecture - Robert C Martin', 'book2': 'The Art of War - Sun Tzu',}
reading_list['book3'] = 'The lean startup - Eric Ries'
print(reading_list)

# We can also overwrite an existing key
reading_list['book2'] = 'By the River - Paulo Coelho'
print(reading_list)

# To see all the keys in a dictionary
dict_keys = reading_list.keys()
print(dict_keys)

# To get all the values in a dictionary
dict_values = reading_list.values()
print(dict_values)

# To get the pairings of the items in the dictionary
dict_pairings = reading_list.items()
print(dict_pairings)
