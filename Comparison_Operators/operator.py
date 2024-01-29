# Comparison operators are for checking the equality

# evaluates to True
ans = 2==2
print(ans)

# We have to use a double equal sign so as python interpreter cannot think we are trying to assign a value to a variable
a = 2
b = 1

c = a == 1 # evaluates to false
print(c)

# When comparing strings capitalization counts

first_string = 'Bye'
second_string = 'bye'

check = first_string == second_string
print(check)

# Python considers types
num1 = '2'
num2 = 2 
eval = num1 == num2
print(eval)

#For floating point as long as they hold the same value they will be true 
number1 = 2.0
number2 = 2
evalnum = number1 == number2
print(evalnum)

# For inequality you use the exclamation sign 

d = 3 
f = 3 
r = 3 != 3
print(r)

# Checking size 

size_num1 = 4 
size_num2 = 5 
check_size = size_num1 > size_num2
print(check_size)
 
reverse = size_num2 < size_num1
print(reverse)

# Equal to

numcode = 2 >= 1
print(numcode)

numcode1 = 1 <= 2
print(numcode1)

# Chaining comparison operators 
# We can use logical operators when chaining comparison operators; and, or , not
variable1 = 1
variable2 = 2
variable3 = 3
variable1 < variable2
variable2 < variable3
1 < 2 
2 < 3

# Can be chained into 
variable1 < variable2 < variable3
1 < 2 < 3

# We could use logical operators 
# And needs both conditions to be true 

multi_check = variable1 < variable2 and variable2 < variable1
print(multi_check)

test = 'h' == 'h' and 2 == 2
print(test)

# or keyword -> needs one condition to be true 
calc = variable1 == variable1 or variable2 == variable2
print(calc)

# Chaining comparison operators using logical operators ensures code readability

# not Keyword  -> returns the opposite boolean of what we just did i.e the predecessor operator
not(1==1) # evaluates to false