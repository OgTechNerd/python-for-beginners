# *args
# The special syntax *args in function definitions in python is used to pass a variable
# number of arguments to a function. It is used to pass a non-keyworded, variable-length argument list.
# The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
# What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
# With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
# For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. 
# It can be done using *args. Using the *, the variable that we associate with the * becomes an iterable meaning you can do things
# like iterate over it, run some higher order functions such as map and filter, etc.# 


# **kwargs
# Python passes variable length non keyword argument to function using *args but we cannot use this to pass keyword argument. 
# For this problem Python has got a solution called **kwargs, it allows us to pass the variable length of keyword arguments to the function.
# In the function, we use the double asterisk ** before the parameter name to denote this type of argument. The arguments are passed as a dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.

def functionone(*argv):
    for item in argv:
        print(item) 

    print(argv[0])

def functiontwo(**kwargs):
    for key , value in kwargs.items():
        print(key, value)

def functionthree(*argv, **kwargs):
    for key , value in kwargs.items():
        if key:
            print(key, value)
        return  False
    if len(argv) != 0:
        for item in argv:
            print(item)
    else:
        print("No arg passed")
functionone('first_arg', 'second_arg', 'third_arg')
kwargs = {"first": "one", "second": "two", "third": "three"}
list = ['wacky', 'divine', 'harsh']
kwargs1 = {'australia': 'tier1', 'united Kingdom':'tier2', 'united states': 'tier3'}
functiontwo(**kwargs)
functionthree(list)
functionthree(kwargs1)