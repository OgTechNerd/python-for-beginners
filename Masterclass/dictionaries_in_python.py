# python provides another compoite data
# type called dictionary which is similar to a list in that it is
# a collection of objects
# Dictionaries and list share the following characteristcs
# both are mutable, both are dynamic
# they can grow and shrink as needed
# both can be nested . A list can contain another list
# A dictionary can be nested . A list can contain another
# list. A dicitonary can contain antoher dictionary
# A dictionary can also contain list.

# Dictionaries are python implementation of data structure
# that is more generally known as associative array.
# A dictionary consist of a clollection of key-Value
# pairs maps the key to associative array

sample_dict = {
    'key1' : 'value1',
    'key2' : 'value2',
    'key3' : 'value3'
}

#  you can also construct dictionary with build -in dict()
#  function .The argument to dict() should be a sequence of
# key value pairs

sal_dict = dict([
    ('shaun', 3000),# these ae tuples , they are immutable
    ('oendrila', 10000),
    ('jhinuk', 50000)
])

person = {}
# building dict incrementally 
person['fname'] = 'joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'edna'
person['children'] = ['ralph', 'betty', 'joseph']
person['pets'] = {'dog': 'fido', 'cat': 'sally'}

print(sample_dict)
print(sample_dict.keys())
print(sal_dict['jhinuk'])
sal_dict['yamraj'] = '10000'
sal_dict['shaun'] = '400000'
del sal_dict['oendrila']
print(sal_dict)
print(type(person))
print(person)
print('spouse' in person)
print('nothing' in person)
# built in dictionary methods
# empties dictionary d of all key-value pairs
sal_dict.clear()
print(person.get('pets'))
print(f"returns a list of key-value paris: {person.items}")
print(person.keys())
print(person.values())
person.pop('age')
# merges a dictionary with another dictionary 
d1 = {'a': 30, 'b': 40, 'c': 50}
d2 = {'b': 40, 'x': 90, 'y': 100}
d2.update(d1)
print(d2)