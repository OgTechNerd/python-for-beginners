
""" Built-In Class Attributes
 Every Python class keeps following built-in attributes and they can be accessed using dot operator
 like any other attribute −
 __dict__: Dictionary containing the class's namespace.
 __doc__: Class documentation string or none, if undefined.
 __name__: Class name.
 __module__: Module name in which the class is defined. This attribute is "__main__" in
 interactive mode.
 __bases__: A possibly empty tuple containing the base classes, in the order of their
 occurrence in the base class list.
 For the above class let us try to access all these attributes """

# added
class Employee(object):
    empCount =0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1
    
    def displayCount(self):
        print(" Total Employee %d" % Employee.empCount)

if __name__ == "__main__":
    obj = Employee("shaun", 90000)
    print(obj.name)
    print("Employee.__doc__ : {}".format(Employee.__doc__))
    print("Employee.__name__: {}".format(Employee.__name__))
    print("Employee.__module__ : {}".format(Employee.__module__))
    #print("Employee.__bases__: {}".format(obj.__bases__))
    print("Employee.__dict__: {}".format(Employee.__dict__))
    