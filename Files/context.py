# Another way to work with files is by using context managers 
# Most effective way

with open('/home/nyae/LearnPython/LearnPython/Files/basic.txt', 'r') as f:

    # Indented code goes here
    # This is ideal when working with small files
    # We can pass in the number of characters we want printed out as an argument to the function read()
    size_to_read = 100 
    contents = f.read(size_to_read)
    while len(contents)>0:
        print(contents, end='')
        contents = f.read(size_to_read)
    """
    # we could also use another method readlines which prints the contents of the file as a list 
    contents = f.readlines()
    print(contents)
    # When using the method readline() it prints out the first line in the file
    # Print statement adds an extra line at the of the output to stop this we add a variable end and assign an empty string to it

    contents = f.readline()
    print(contents, end='')
    
    contents = f.readline()
    print(contents, end= '')

    """
    """
    # For large files we iterate through the line it wont run down our memory
    for line in f:
        print(line, end='')
    """