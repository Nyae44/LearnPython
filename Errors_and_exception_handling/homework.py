"""
Problem 1
Handle the exception thrown by the code below by using try and except blocks.
"""

for i in ['a','b','c']:
    try:
        print(1**2)
    except TypeError: 
        print("Found a TypeError")
        
"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
"""
x = 5
y = 0

try:
    print(x/y)
except ZeroDivisionError:
    print("Found a ZeroDivisionError")
finally:
    print('All done')

"""
Problem 3
Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
"""
def ask():
    while True:
        try:
            ask_for_int = int(input("Please provide an integer: "))
        except:
            print("An error occurred! Please try again")
            continue
        else:
            ask_for_int **= 2
            print("Thank you, your number squared is: {}".format(ask_for_int))
            break
              
test_ask = ask()
print(test_ask)