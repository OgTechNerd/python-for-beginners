# NumPy is the fundamental Python package for scientific computing. It adds the capabilities  of N-dimensional arrays, element-by-element operations (broadcasting), core
# mathematical operations like linear algebra, and the ability to wrap C/C++/Fortran  code.We will cover most of these aspects in this chapter by first covering

# The NumPy package enables users to overcome the shortcomings of the Python lists by providing a data storage object called ndarray.
# The ndarray is similar to lists, but rather than being highly flexible by storing different types of objects in one list, only the same type of element can be stored in each column.
# For example, with a Python list, you could make the first element a list and the second another list or dictionary. With NumPy arrays, you can only store the same type of
# element, e.g., all elements must be floats, integers, or strings. Despite this limitation, ndarray wins hands down when it comes to operation times, as the operations are sped
# up significantly. Using the %timeit magic command in IPython, we compare the power of NumPy ndarray versus Python lists in terms of speed.
#!/usr/bin/Python3
import numpy as np

#array1 = np.arange(1e7)
#array2 = array1.tolist()
#print(array1, array2)

arr1 = np.arange(15).reshape(3, 5)
print(arr1)
print(" shape : {0} dimension: {1} type: {2} itemsize: {3}".format(arr1.shape, arr1.ndim, arr1.dtype, arr1.itemsize ))
