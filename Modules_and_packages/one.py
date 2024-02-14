# When you run a block of python code at the terminal, all the code at indentation level zero gets executed
print("Hello")

# In Python, there is a built in variable called __name__
# When running python one.py from terminal,the built in variable is assigned a string on the background __name__ = "__main__"
# Which in turn allows us to do something like adding an if statement before it

def func():
    print("FUNC() IN one.py")

print("TOP LEVEL IN one.py")

if __name__ == "__main__":
    print("one.py is being run directly!")
else: 
    print("one.py has been imported!")

