# Special methods allow us to use built Python operators with our own user defined methods 

# Example in checking length, we use the len keyword

my_list = [1,2,3]
print(len(my_list))

# Case : Using built in Python functions with user defined objects 
class Sample():
    pass

my_sample = Sample

print(my_sample)


# This is where special methods come into play

class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    
    # The string method is a special method that dictates how an object should be represented as a string
    # You should always use a return statement on the special string method 
    
    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} pages"
   
    # To get the length of the object we use the special method __len__
    def __len__(self):
        return self.pages
    
    # If you want special things to happen when you delete an item you call a __del__ method
    
    def __del__(self):
        print('A book object has been deleted')
    
b = Book('The Art of War', 'Sun Tzu', 300)
print(b)

print(len(b))

# We can also delete elements from memory i.e book using the b keyword 
del b # deletes the book 