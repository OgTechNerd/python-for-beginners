# Generators are functiosn that can be paused and resumed on the
# fly , returning an object that can be iterated over.
# unlike  lists, they are lazy and thus produce items
# one at a time and only when asked. So they are much more 
# memory efficient when
# dealing with large datasets.The article below talks
# about how to create generator functions
# and expressions as well as why you should want to use them
# in the first place

def count(num):
    print('Starting')
    while num > 0:
        yield num
        num = -1
val = count(10)
print (next(val))

# Generator Expresions , generator can also be writen in the
# same manner except they return a generator object
# rather than a list

gen_list = ['a', 'b', 'v', 'x', 'y']
for val in gen_list:
    print(val)
gen_obj = (x for x in gen_list)
for val1 in gen_obj:
    print(val1)
import sys
g = (i * 2 for i in range(1000) if i % 3 == 0)
print(sys.getsizeof(g))
# Generators are perfect for reading a 
# large number of large files since they 
# yield out data a single chunk at a time 
# irrespective of the size of the input stream. 
# They can also result in cleaner code by decoupling 
# the iteration process into smaller components.

import os 
def generate_filenames():
    """
    generate a sequence of opened files
    matching a specific extension
    """
    #lines = []
    for dir_path, dir_names, file_names in os.walk('test/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                yield open(os.path.join(dir_path, file_name))

def cat_files(files):
    """
    takes in an iterable of filenames
    """
    for fname in files:
        for line in fname:
            yield line

def grep_files(lines, pattern=None):
    """
    takes in an iterable of lines
    """
    for line in lines:
        if pattern in line:
            yield line


py_files = generate_filenames()
py_file = cat_files(py_files)
lines = grep_files(py_file, 'python')
for line in lines:
    print (line)