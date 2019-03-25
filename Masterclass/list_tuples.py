# Lists and tuples are arguably Python’s most versatile, 
# useful data types. You will find them in virtually every nontrivial Python program.
# Here’s what you’ll learn in this tutorial: You’ll cover the important characteristics of lists and tuples.
# You’ll learn how to define them and how to manipulate them. When you’re finished, you should have a good feel 
# for when and how to use these object types in a Python program.
# Python Lists In short, a list is a collection of arbitrary objects, 
# somewhat akin to an array in many other programming languages but more flexible. 
# Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([]), 
# as shown below:
# The important characteristics of Python lists are as follows: 
# Lists are ordered.
# Lists can contain any arbitrary objects.
# List elements can be accessed by index.
# Lists can be nested to arbitrary depth.
# Lists are mutable.
# Lists are dynamic.

SampleList = ['string1', 'string22', 'string3', 'string4']
a = [21.42, 'foobar', 3, 4, 'bark', False, 3.14159]
print(f" {a[0]}, {a[-1]}, {a[-2]}, {a[-3]}, {a[-4]}")
print(f" {a[0]}, {a[1]}, {a[2]}, {a[3]}, {a[4]}")
## slicing of list
print(a[2:5])
## reverse a list
print(a[::-1])
print(len(SampleList))
print(min(SampleList))
print(max(SampleList))
a.append("pond")
a.append([1,2,3])
a.extend([5, 6, 7])
print(a)
x = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
x.pop(2)
x.insert(0, 2.3)
print(x)
x.remove('qux')
print('bar' not in x)
 

# Python Tuples
# Python provides another type that is an ordered collection 
# of objects, called a tuple.Pronunciation varies depending 
# on whom you ask. Some pronounce it as though it were spelled
# “too-ple” (rhyming with “Mott the Hoople”), and others as though it were spelled “tup-ple” (rhyming with “supple”). My inclination is the latter, since it presumably derives from the same origin as “quintuple,” “sextuple,” “octuple,” and so on, and everyone I know pronounces these latter as though they rhymed with “supple.”

# Defining and Using Tuples
# Tuples are identical to lists in all respects, 
# except for the following propertie
# tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
# Tuples are immutable.

exampletuple = ('all', 'that', 'glitters', 'is', 'gold')
print(exampletuple)
string1 =""
# converting tuple to string
for item in exampletuple:
    string1 +=item+"\t"
print(string1)


## join function can join all char in list

def convert(s):
    str = ""
    return (str.join(s))

s = ['g', 'u', 'd', 'morning']
print(convert(s))

list1 = ['wow', 'this', 'is', 'list']
#converting list1 to tuple
var4 = tuple(list1)
tuple = ('wow', 'this', 'is', 'tuple')
var3 = list(tuple)
print(type(var3))
print(type(var4))