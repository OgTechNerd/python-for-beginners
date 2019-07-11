# Working with Doc Opts
# In order to add an option we add a <name> 
# to the docstring . They <> are used to designate
# a postional argument. i order to exeute the 
# current logic we must check if the command is 
# true  at runtime if argument['arg']. Then call
# the correct fuction
"""Greeter.

Usage:
  basic.py customer <name>
  basic.py producer <name>
  basic.py (-h | --help)

Options:
  -h --help     Show this screen.

"""
from docopt import docopt


def customer(name):
    print('customer, {0}'.format(name))


def producer(name):
    print('producer, {0}'.format(name))

if __name__ == '__main__':
    arguments = docopt(__doc__)

    print(arguments)
    # if an argument called customer was passed, execute the customer  function 
    # if an argument called producer was passed it will execute the producer function
    # the <name> is the second argument however first argument is the identifier 
    print(arguments.keys())
    if arguments['customer']:
        customer(arguments['<name>'])
    elif arguments['producer']:
       producer(arguments['<name>'])
    print(arguments['<name>'])