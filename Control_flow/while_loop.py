# While continues to execute a block of code while some condition remains true
# While my pool is not full, keep filling my pool with water or While my dogs are hungry, keep feeding my dogs 

# Syntax for While loop
"""
while some_boolean_condition:
    # do something
"""
# We can also combine a while loop with an else statement if we want 
"""
while some_boolean_condition:
    # do something
else:
    # do something different

"""

# Example  

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
else:
    print('X is not LESS then 5')

# There are three main keywords associated with loops in Python
# Break -> Breaks out of the current closest enclosing loop
# Continue -> Goes to the top of the closest enclosing loop
# Pass -> Does nothing at all
    
x = [1,2,3]
 
# Pass does nothing at all
for num in x:
    #Comment -> You get an unexpected EOF while parsing EOF - END OF FILE - The pass keyword helps avoid a syntax error
    pass
print('End of my script')

# Continue -> Goes to the top of the closest enclosing loop
name = 'Daley'

for letter in name:
    # The letter a will not be printed since the program will go to the top of the enclosing loop
    if letter == 'a':
        continue
    print(letter)

# Break -> Breaks out of the current closest enclosing loop


city = 'Nairobi'
for char in city:
    # The program will only print the values before 'a' and stop i.e N
    if char == 'a':
        break
    print(char)


# In while loops 
    s = 0
    while s < 5:
        if s == 2:
            break
        print(f'S is {s}')
        s += 1