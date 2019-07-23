# Object oriented python
# creating sample class

# What Is Object-Oriented Programming (OOP)?

# Object-oriented Programming, or OOP for short, is a programming paradigm which provides a means of structuring programs 
# so that properties and behaviors are bundled into individual objects.
# For instance, an object could represent a person with a name property, age, address, etc.,
# with behaviors like walking, talking, breathing, and running. Or an email with properties like 
# recipient list, subject, body, etc., and behaviors like adding attachments and sending.
# Put another way, object-oriented programming is an approach for modeling concrete, 
# real-world things like cars as well as relations between things like companies and employees, students and teachers, etc.
# OOP models real-world entities as software objects, which have some data associated with them and can perform certain functions.
# Another common programming paradigm is procedural programming which structures a program like a recipe in that it provides a set of steps,
# in the form of functions and code blocks, which flow sequentially in order to complete a task.
# The key takeaway is that objects are at the center of the object-oriented programming paradigm, not only representing the data, 
# as in procedural programming, but in the overall structure of the program as well.

# Python Objects (Instances)
# While the class is the blueprint, an instance is a copy of the class with actual values, 
# literally an object belonging to a specific class. It’s not an idea anymore; it’s an actual animal, 
# like a dog named Roger who’s eight years old.
# Put another way, a class is like a form or questionnaire. It defines the needed information. 
# After you fill out the form, your specific copy is an instance of the class; it contains actual information relevant to you.
# You can fill out multiple copies to create many different instances, but without the form as a guide, you would be lost, 
# not knowing what information is required. Thus, before you can create individual instances of an object, 
# we must first specify what is needed by defining a class.

class vehicle(object):
    # class variable
    variable1 = "This is class variable, anyone can access from class"

    # This is default constructor
    def __init__(self, manufacturer, model, price, horsepower):
    ## these are called instance attributes
        self.model = model
        self.price = price
        self.horsepower = horsepower
        self.manufacturer = manufacturer
        self.gear = False
    
    # Instance Attributes are unique to each object, (an instance is another name for an object). Here,
    # any Dog object we create will be able to store its name and age. We can change either attribute of either dog,
    # without affecting any other dog objects we’ve created.

##class Dog:
    
## def __init__(self, name, age):
##    self.name = name
##    self.age = age

# This __init__ is called the initializer. It is automatically called when we instantiate the class. 
# It’s job is to make sure the class has any attributes it needs. It’s sometimes also used to make sure that the object
# is in a valid state when it’s instantiated, like making sure the user didn’t enter a negative age for the dog.
# We have to include the self parameter so that our initializer has a reference to the new object being instantiated.

# Class Attributes are unique to each class. Each instance of the class will have this attribute. 
# It’s sometimes used to specify a defualt value that all objects should have after they’ve been instantiated. 
# Here, our class attribute is species

# class Dog:

#    species = 'mammal'
#     def __init__(self, name, age):
#        self.name = name
#        self.age = age

    # A class method is a method that is bound to a class rather than its object. 
    # It doesn't require creation of a class instance, much like staticmethod.
    # The difference between a static method and a class method is:
    # Static method knows nothing about the class and just deals with the parameters
    # Class method works with the class since its parameter is always the class itself.


    @classmethod
    def sportscar(cls):
        return cls("lamborghini", "hur", 100000000, 15000)
        
    @classmethod
    def bogus(cls):
        return cls("maruti", "alto", 1000, 150)


    # This is  not a class method
    def milage(self):
        if (self.horsepower >= 1000):
            print( "Mileage will be poor")
        else:
            print( "Mileage will be good")

if __name__ == "__main__":
    car1 = vehicle('ford', 'gt', 2000000, 800)
    print(car1.model)
    print(vehicle.variable1)
    print(car1.variable1)
    print(car1.milage())
    car2 = vehicle.sportscar()
    print(car2.milage())