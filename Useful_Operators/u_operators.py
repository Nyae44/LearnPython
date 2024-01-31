# There are useful operators in Python that help a great deal when programming in Python
# Range ->  We can perform iteration using this built in operator i.e
# The range operator has the following parameters range(start,stop,jump)
# Example -> prints numbers from zero to nine with an exception of 10 
for num in range(10):
    print(num, end=' ')

# We can also add step size to the range function i.e a step size of 2 prints all the even numbers 

for number in range(10,2):
    print(number)

# We can also define the starting point with the range function i.e prints numbers from 4 -9

for item in range(3,10,1):
    print(item)

# The range function is a generator hence can be used to generate a list i.e prints a list from 0-10 with a stepsize of 2
created_list = list(range(0,11,2))
print(created_list)

# Enumerate -> Allows you to iterate through a sequence keeping track of the index of each element

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))

    index_count += 1

# Another example prints word from a to f in order of its indexes
index_compute = 0
word = 'abcdef'
for letter in word:
    print(word[index_compute])
    index_compute +=1

# The above example can be done using the enumerate keyword 

for item in enumerate(word):
    print(item)

# We could also do tuple unpacking since the above enumerate example results to a tuple

for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# Zip -> Pairs up items in two different lists 
    
my_list1 = [1,2,3]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1,my_list2):
    print(item)

# We could perform tuple unpacking since the zip functions prints out a tuple
for index, letter in zip(my_list1,my_list2):
    print(index)
    print(letter)
    print('\n')

# We could use the zip function with more two lists i.e
my_list3 = [100,200,300]

for item in zip(my_list1,my_list2,my_list3):
    print(item)

# Tuple unpacking for more than two lists
    for index, letter, quantity in zip(my_list1,my_list2,my_list3):
        print(index)
        print(letter)
        print(quantity)
# We can also cast it in a list i.e 
savezip = list(zip(my_list1,my_list2,my_list3))
print(savezip)

# In Keyword -> Used to check if something is in a list 
new_list = [3,4,5,7,8]
checker = 'X' in new_list
print(checker)

# It also works in other iterable types i.e strings 
name = 'Amina'

wordchecker = 'a' in name
print(wordchecker)

# Also works in dictionary keys 
d = {'myKey': 345, 'yourKey':678}
dictchecker = 'myKey' in d.keys()
print(dictchecker)

# You could also check in values 
valuechecker = 345 in d.values()
print(valuechecker)

# Min -> checks for the minimum value in a list 

sales_records = [10,20,30,40,50,60,70,80,90,100]
print(min(sales_records))

# Max -> checks for the maximum value in a list 
print(max(sales_records))

# Random library -> contains a number of random number generation related functions
# shuffle is an in place function meaning it doesnt need to be assigned to a variable
from random import shuffle
work_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(work_list)
print(work_list)

# randint -> Allow us to grab a random integer 
# randint(lower bound, upper bound)
from random import randint
track_code = randint(100000,200000)
print(track_code)


# How to accept user input

favourite_number = input('Enter your favorite number: ')
print(favourite_number)

# By default user input returns a string you could wrap it to your data type of choice i.e

tracking_number = int(input('Enter your tracking number: '))
print(type(tracking_number))