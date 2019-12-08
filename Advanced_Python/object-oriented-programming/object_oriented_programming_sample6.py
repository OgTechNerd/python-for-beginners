# We will be explaining how inheritance works.
# Inheritance is the capability of one class to derive or inherit the properties from some another class.
# The benefits of inheritance are: 
# It represents real-world relationships well.
# It provides reusability of a code. We don’t have to write the same code again and again. 
# Also, it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A,
# then all the subclasses of B would automatically inherit from class A.
# In Python we have a class User which is the parent class

#######################################################################################################
############ PARENT CLASS
#######################################################################################################
class user():
    persontype = 'Miser'
    def __init__(self, name, age, sex, company, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.company = company
        self.salary = salary
# This is instance method
    def does_work(self):
        print('This guy works for {}'.format(self.company))
# These are dunder  methods or magic methods
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores
# in the method name. Dunder here means “Double Under (Underscores)”. These are commonly used for operator 
# overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
# The __init__ method for initialization is invoked without any call, when an instance of a class is created, 
# like constructors in certain other programming languages such as C++, Java, C#, PHP etc. 
# These methods are the reason we can add two strings with ‘+’ operator without any explicit typecasting.
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        return "Name: {} , age: {} ,sex: {}, status: {}, salary: {}".format(self.name, self.age, self.sex, self.company, self.salary)
# This is a class method. This can access class variables and change the value.
    @classmethod
    def type_of_person(cls):
        persontype = "rich"
        print('This person is a {}'.format(persontype))
# This is a static method. This can only access class attributes and not class variable
    @staticmethod
    def earning(salary):
        print('This persons bonus is {}'.format(salary))


##################################################################################################
############ Child Class
##################################################################################################
class  Developer(user):
    def isUser(self):
        return True
    def __repr__(self):
        return super().__repr__()
    def __str__(self):
        return super().__str__()
    def does_work(self):
        return  print('This guy is Developer  for {}'.format(self.company))





if __name__ == "__main__":
    player1 = user('Arindam', '66', 'male', 'IBM', '25000')
    print(str(player1))
    print(repr(player1))
    # Instance method execution
    player1.does_work()
    print(user.persontype)
    # Class Method execution
    user.type_of_person()
    player1.type_of_person()
    player1.earning(5000)
    user.type_of_person()
    player2 =Developer('Jhinuk', '33', 'female', 'TCS', '99000')
    player2.does_work()



