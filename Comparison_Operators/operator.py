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