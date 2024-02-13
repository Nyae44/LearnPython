# Assignment
"""
Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
"""
class Line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        
    def distance(self):
        return (((self.coor2[0]-self.coor1[0])**2)+((self.coor2[1]-self.coor1[1])**2)) **0.5
    def slope(self):
        return ((self.coor2[1]-self.coor1[1])/ (self.coor2[0]-self.coor1[0]))
        
coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

# Calculate the distance between the two coordinates 
print(li.distance())

# Calculate the slope/gradient 

print(li.slope())

"""
Problem 2
Calculate the Volume and surface area of a cylinder
"""

class Cylinder():
    
    pi = 3.142
    def __init__(self,height = 1, radius = 1):
        self.height = height
        self.radius = radius
    def volume(self):
        # pi * r ** 2
        return (Cylinder.pi * self.radius * self.radius)
    
    def surface_area(self):
        # (2 * pi * r * height) + (2 * pi * r * r)
        return ((2 * Cylinder.pi * self.radius * self.height) + (2 * Cylinder.pi * self.radius * self.radius))
        

c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())




