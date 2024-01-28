# Working with files
# Create a file in the same location your scripts are running 
# Provide the full correct file path /home/nyae/LearnPython/LearnPython/Files/
myfile = open('/home/nyae/LearnPython/LearnPython/Files/basic.txt', 'r')
# myfile.read() 
# print(myfile.read())
# To print file name
print(myfile.name) 

# To check the mode that we are in it should print r to mean that we are on read mode

print(myfile.mode)

# We have to explicitly close the file 
myfile.close()
# Using the with statement to read files
with open('/home/nyae/LearnPython/LearnPython/Files/basic.txt', mode= 'r') as newfile:
    contents = newfile.read()
    print(contents)
# How to add a new line to the file
    with open('/home/nyae/LearnPython/LearnPython/Files/basic.txt', mode='a') as addline:
        content_data = addline.write('\n this is the fourth line')
        print(content_data)
# How to overwrite an existing file or creating a new file 
    with open('/home/nyae/LearnPython/LearnPython/Files/new.txt') as f:
        latest = f.write('I created this file')
        print(latest)
        # I get a traceback error which i'll figure out later, I'm hungry