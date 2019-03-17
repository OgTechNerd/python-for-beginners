import datetime
class complex(object):
    def  __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __repr__(self):
        return  'rational(%s, %s)' % (self.real, self.imag)
    def __str__(self):
        return  '%s + i%s' %(self.real, self.imag)
    @staticmethod
    def somemethod(num):
        z = num * 10
        return f"value is {z}"
# Every module in python has a special attribute called __name__ . 
# The value of __name__  attribute is set to '<strong>main</strong>'
# when module run as main program. Otherwise the value of __name__  
# is set to contain the name of the module.
if __name__ == "__main__":
    object1 = complex(10, 40)
    print(repr(object1))
    print(str(object1))
    print(object1.somemethod(5))
    today = datetime.datetime.now()
    print(repr(today))
    print(str(today))
# str() displays today’s date in a way that the user can understand the date and time.
# repr() prints “official” representation of a date-time object (means using the “official” 
# string representation we can reconstruct the object).
# How to make them work for our own defined classes? 
# A user defined class should also have a __repr__ if we need detailed information for debugging. 
# And if we think it would be useful to have a string version for users, we create a __str__ function.