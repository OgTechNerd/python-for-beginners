import re

text_to_search = '''
abcdefghijklmnopqrst
ABCDEFGHIJKLMNOPQRSTUVWXYZ
123456789

'''

#pattern = re.compile(r'\D')
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)
for match in matches:
	print(match)
