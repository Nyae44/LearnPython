# Displaying information
# Instead of printing each item or row we can enclose it in a funct


from curses.ascii import isdigit
from random import choice


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

example_row = [1,2,3]
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

row2[1] = 'X'
display_this = display(row1,row2,row3)
print(display_this)

# Accepting user input

result = input('Please enter a value: ')

result_int = int(result)

position_index = int(input('Choose an index position: '))
value_at = row2[position_index]
print(value_at)

# Validating user input

def user_choice():
    # Variables

    # Initial value
    choice = 'Wrong'
    acceptable_range = range(0,10)
    within_range = False
    # Two conditions to check
    # Digit or within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number(0-10): ')

        # Digit check
        if choice.isdigit == False:
            print('Sorry that is not a digit!')
        # Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry you are out of acceptable range')
                within_range = False
    return int(choice)

user_choice_call = user_choice()

print(user_choice_call)