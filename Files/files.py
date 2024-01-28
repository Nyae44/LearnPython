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