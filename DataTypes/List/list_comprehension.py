# This short course breaks down Python list comprehensions for yuo step by step
# see how python's comprehensions can be transformed from and to equivalent for loops 
# so you wil  know exactly what's going on behind the scenes
# one of the favourite features in Python are list comprehension.
# they can seem a bit arcane at first but when you break them down
# they are actually very simple constructs.
# list comprehensions

squares = [x * x for x in range(10)]
add = [x + x for x in range(5)]
slist = ['sachin', 'sourav', 'dravid']
list1 = [item for item in slist if item.startswith('s')]
# Best practices to use list comprehensions
# values = [ expression] 
print(add)
print(squares)
print(list1)