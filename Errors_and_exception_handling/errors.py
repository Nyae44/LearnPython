# Error handling is used to plan for possible errors
# In Error handling the code does not stop if it finds an error, it reports the error and continues 
from unittest import result


def add(n1,n2):
    print(n1+n2)


number1 = 10

number2= int(input("Please enter a number: "))

test_result = add(number1,number2)
print("Something happens")
print(test_result)

try: 
    # Want to attempt this code
    # May have an error
    test_result = 10 + 10
except:
    # Block of code will execute in case there is an error in try block
    print("Hey! it looks like you aren't adding correctly")
else:
    print('Add went well')
    print(test_result)
    
    
try:
    f = open('testfile', 'w')
    f.write("Write a test line!")
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey you have an OSError')
finally:
    print('I always run')
    
# Error handling in a function that accepts input from a user 
def ask_for_int():
    # Enclose in a while loop so it continually requests for a number 
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! that is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end")

test_ask_for_int = ask_for_int()
print(test_ask_for_int) 
