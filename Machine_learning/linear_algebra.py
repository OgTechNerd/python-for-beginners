# NumPy arrays do not behave like matrices in linear algebra by default. Instead, the
# operations are mapped from each element in one array onto the next. This is quite
# a useful feature, as loop operations can be done away with for efficiency. But what
# about when transposing or a dot multiplication are needed? Without invoking other
# classes, you can use the built-in numpy.dot and numpy.transpose to do such operations.
# The syntax is Pythonic, so it is intuitive to program. Or the math purist can use
# the numpy.matrix object instead. We will go over both examples below to illustrate
# the differences and similarities between the two options. More importantly, we will
# compare some of the advantages and disadvantages between the numpy.array and the
# numpy.matrix objects. Some operations are easy and quick to do in linear algebra. A classic example is solving
# a system of equations that we can express in matrix form:

import numpy as np

arr1 = np.matrix([[3, 6, 5], [1, -3, 2], [12, -2, 10]])
arr2 = np.matrix([[12], [-2], [10]])

# Inverting the array
# Now let us represent the matrix system as AX = B, and solve for the variables. This
# means we should try to obtain X = A−1B. Here is howwe would do this withNumPy.
X = arr1 ** (-1) * arr2
print(X)

a = np.array([[3, 6, -5],
[1, -3, 2],
[5, -1, 4]])
# Defining the array
b = np.array([12, -2, 10])
# Solving for the variables, where we invert A
x = np.linalg.inv(a).dot(b)
print(x)
# array([ 1.75, 1.75, 0.75])