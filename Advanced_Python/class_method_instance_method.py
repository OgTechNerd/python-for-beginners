# What’s the difference between @classmethod, @staticmethod, and “plain/regular” instance methods in Python?
# You’ll know the answer after watching this video course:
# Regular (instance) methods need a class instance and can access the instance through self. 
# They can read and modify an objects state freely.

# Class methods, marked with the @classmethod decorator, don’t need a class instance. 
# They can’t access the instance (self) but they have access to the class itself via cls.
# Static methods, marked with the @staticmethod decorator, don’t have access to cls or self. 
# They work like regular functions but belong to the class’s namespace.

# In this course you’ll go over the differences between these three kinds
# of methods in Python. You’ll also see when to use each with a simple example, 
# so you can improve your object-oriented programming (OOP) skills in Python.

class DemoClass:
    def demo_instancemethod(self):
        return " Demo Instance Method called", self
    
    # cant modify object instance state
    # can modify the class state
    @classmethod
    def demo_classmethod(cls):
        return "Demo Class Method called", cls


    ## has no access to class state or instance object instance state    
    @staticmethod
    def demo_staticmethod():     
        return " Demo Static Method called"



newObj = DemoClass()
print(newObj.demo_instancemethod())
print(newObj.demo_classmethod())
print(newObj.demo_staticmethod())