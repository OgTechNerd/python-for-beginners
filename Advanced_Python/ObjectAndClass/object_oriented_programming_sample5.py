# Class inheritance Instead of starting from
# scratch you can create a class by deriving it
# pre exisitinf class by listing the
# the parent class in the parenthesis
# after the new class name
# The child class inherits the attribute of its parent class
# and you can use those attrbutes 
# as if they were defined in the child class
# A child class can also override data members and methods
# from the parents
class Polygon(object):
    def __init__(self, s):
        self.s = s
  
    def getSides(self, s, dimension):
        self.s = s
        self.dimension = dimension
        print(f"The sides are {self.s} and dimension is {self.dimension}")
    
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self,  base, height):
        area = base ** height ** 0.5
        print(f'The area of the triangle is {area} sqcm')

if __name__ == "__main__":
    cobject1 = Triangle()
    cobject1.findArea(8, 6)
    cobject1.getSides(3, 2)
    #cobject1.findArea()

    