# Generators allow us to send back a value and then later pick it up where it left off

# func creates cubes from zero upto n 
# notice the  pattern and how the entire list is kept in memory


def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

test_create_cubes = create_cubes(10)
#print(test_create_cubes)

# instead of creating that giant list, its better to yield it into actual key numbers 
def efficient_code(n):
    for x in range(n):
        yield x**3
# create cube is an object in memory, for it to return actual values 
# you have to iterate through it or cast it to a list i.e list(create_cubes)
for num in efficient_code(15):
    print(num)

# fibonacci sequence

def gen_fibonacci(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a,b = b,a +b
        
for number in gen_fibonacci(10):
    print(number)
    
    
# more understandable example 
def simple_gen():
    for x in range(3):
        yield x
        
        
for num in simple_gen():
    print(num)
    
# using the next keyword 
g = simple_gen()

print(next(g))
print(next(g))
print(next(g))

# The above example is what the generator does when you return the yield keyword,
# It remembers the previous value and returns the next one
# All this is not done in memory 


# iter() function
# Allows us to automatically iterate through a normal object

s = 'hello'
for letter in s:
    print(letter)
 
# we can use the next keyword in the example below
# TODO: Explain why the iter() function iterates    
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
