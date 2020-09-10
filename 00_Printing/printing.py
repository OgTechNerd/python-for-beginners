# This exercise we are going to print  single line  and multi line comments
# The following examples will help you understand the different ways of 
# printing 

import pprint 
from tabulate import tabulate
from prettytable import PrettyTable
print ("Mary had a little lamb")
print ("Its Fleece was white as %s ." % 'snow')
print('Mercury', 'Venus', 'Earth', sep=', ', end=', ')
print('Mars', 'Jupiter', 'Saturn', sep=', ', end=', ')
print('Uranus', 'Neptune', 'Pluto', sep=', ')

# Using Newline Character with extra padding
print('Printing in a Nutshell', end='\n * ')
print('Calling Print', end='\n * ')
print('Separating Multiple Arguments', end='\n * ')
print('Preventing Line Breaks')

pp =pprint.PrettyPrinter(indent=4, depth=2, width=80)
grocery = ['eggs', 'bread', 'milk']
pp.pprint(grocery)
print(pprint.isreadable(grocery))
print(tabulate([['Arindam', 50000], ['Shaun', 30000]], headers=['Name', 'Salary'], tablefmt='orgtbl'))
table = PrettyTable(['Name', 'PhNo'])
table.add_row(['Sourav', 979136789])
table.add_row(['Sachin', 8792798890])
print(table)

# String formatting is attractively designing your string using formatting techniques 
# provided by the particular programming language. We have different string formatting 
# techniques in Python. We are now going to explore the new f-string formatting technique.
# f-string evaluates at runtime of the program. It's swift compared to the previous methods.
# f-string having an easy syntax compared to previous string formatting techniques of Python. 
# We will explore every bit of this formatting using different examples
Company = "Wipro"
Incentive = "Nothing"

print(F"Company {Company} is giving {Incentive} as incentive for year 2020")