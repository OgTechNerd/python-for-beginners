# String Manipulation 
# highlights the operators metods 
# functions that are available for working with strings
# the  + operator concatenates 

x = 'Foo'
y = 'Bar'
z = 'Baz'

print(x + y +z)
print(x * 4)

s = 'say'

print(s in "say what brother")
# built in string functions
# chr() converts an integer to a character
# ord() converts a character to an integer
# len() returns the length of a string
# str() returns a string representation of an object
print(ord('a'))
print(chr(190))
s  = "bhag bhag Dk bose"
print(len(s))
print(str(3+30))

string1 = 'moonlit night , on the beach'
print(string1[7:30])
string2 = 'foobar'
print(string2[:4])
print(string2[0:6:2])
s2 = s.replace('b', 'h')
print(s2)
print(s2.count('h'))
print(string2.endswith('bar'))



