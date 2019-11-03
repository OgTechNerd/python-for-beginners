# Python and other languages like Java, C#, and even C++ have had lambda functions 
# added to their syntax, whereas languages like LISP or the ML family of languages, 
# Haskell, OCaml, and F#, use lambdas as a core concept. Python lambdas are little,
# anonymous functions, subject to a more restrictive but more concise syntax than 
# regular Python functions.The identity function, a function that returns its argument,
# is expressed with a standard Python function definition using the keyword def as follows

def identity(x):
     return x

# identity() takes an argument x and returns it upon invocation.
# In contrast, if you use a Python lambda construction, you get the following:
# In the example above, the expression is composed of:
# The keyword: lambda
# A bound variable: x
# # A body: x
# Note: In the context of this article, a bound variable is an argument to a lambda function.
# In contrast, a free variable is not bound and may be referenced in the body of the expression. 
# A free variable can be a constant or a variable defined in the enclosing scope of the function.

add_one = lambda x: x + 1
add_one(4)
# Map
# The built-in function map() takes a function as a first argument
# and applies it to each of the elements of its second argument, an iterable.
# Examples of iterables are strings, lists, and tuples. 
# For more information on iterables and iterators, check out Iterables and Iterators.
list(map(trace(lambda x: x*2), range(3)))

# Python’s map() is defined as map(function, iterable, ...) and returns
# an iterator that applies function to every item of iterable, yielding
# the results on demand. So, map() could be viewed as an iteration tool
# that you can use to iterate through a dictionary in Python.

# Suppose you have a dictionary containing the prices of a bunch of products,
# and you need to apply a discount to them. In this case, you can define a function
# that manages the discount and then uses it as the first argument to map().
# The second argument can be prices.items():

def discount(current_price):
     return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices.items()))
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}

# filter() is another built-in function that you can use to iterate through a
# dictionary in Python and filter out some of its items. This function is defined as 
# filter(function, iterable) and returns an iterator from those elements of iterable 
# for which function returns True.

# Suppose you want to know the products with a price lower than 0.40. 
# You need to define a function to determine if the price satisfies that
# condition and pass it as first argument to filter(). The second argument 
# can be prices.keys():

prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices[price] < 0.4

low_price = list(filter(has_low_price, prices.keys()))
