# Decorators in python 
# A decorator is a function that takes another function 
# as an input and extends behaviour of that function
# without explicitly modifying the function

# We will cover First class objects 
# Inner Functions
# Returning Function from Functions
# Decorators and Real world examples

def my_sample_function(string):
    """docstrings"""
    return (string+" Banchod chele")


function = my_sample_function("somnath")
print(function)
refference_func = my_sample_function
print(refference_func)
# functions are first class objects 
# functions can  be passed as arguments
# function can be passed to another function as argument
# functions can be added to list like variables

def KissMe(name):
    return (name + " You kissed me")
def HugMe(name):
    return (name + " you hugged me")
def BangMe(name):
    return (name + " you Banged me")

list_rel = [KissMe, HugMe, BangMe]
print(list_rel)
for item in list_rel:   
    print(item("Johny Sins"))

## passing a function as an argument to another functions

def funct1(function):
    print('executing the function passed')
    function('Oh Yeah')

def funct2(string):
    if (string == 'Oh Yeah'): 
        print('Guy is happy')
    else:
        print("Something is wrong")

funct1(funct2)

##  Nested Functions 

def parent(num):
    print("print from the parent")
    def first_child():
        print("printing from first_child")
    def second_child():
        print("printing from seconds_child")
    if num == 1:
        return first_child()
    else:
        return second_child()

first = parent(1)
second = parent(2)


# So till now we have observed function passed as argument to functions
# function return functions
# function refrenced to  varaible as function
# Now Lets discuss about decorators 
# decorators are wrappers around a function. The decorator functions
# accepts a function as a argument

# simple decorator
def sample_decorator(func):
    def wrapper():
        print("Before executing function")
        func()
        print("After executing function")
    return wrapper

@sample_decorator
def demo_func():
    print("Woo Hoo")

# Decorator accepting argument
def sample_decorator1(func):
    def wrapper(name):
        print("Before executing function")
        func(name)
        print("After executing function")
    return wrapper

@sample_decorator1
def demo_func1(name):
    print(f"Woo Hoo {name}")

demo_func1('Guten Morgan')



# the Decorator function

def powerDec(func):
    def wrapper(num):
        print("running Wrapper")
        func(num)
        func(num)
    return wrapper
     
## The syntactic sugar
@powerDec
def squareFunc(num):
    y = num * num
    print(y)
#return y 
squareFunc(5)
    


# decorator returning a function

def dec_shaun(func):
    def wrapper(*args,  **kwargs):
        func(*args,  **kwargs)
        return func(*args, **kwargs)
    return wrapper

def return_greet(name):
    print("Hey welcome to decorators")
    return f"Hey {name} welcome to decorator"

var1 = return_greet("Shaun")
print(var1)