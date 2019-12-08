example_list = range(-5, 10)
less_than_zero = list(filter(lambda x: x < 0, example_list))
print(less_than_zero)

example_dict1 = {'name': 'wonderwoman', 'address': 'santa clara', 'age': '26'}
example_dict2 = {'name': 'superman', 'address': 'california', 'age': '39'}
example_dict3 = {'name': 'batman', 'address': 'san diego', 'age': '45'}


################################
### Filtering Dictionary
################################
list2 = [example_dict1, example_dict2, example_dict3]
for item in list2:
    if (item['address'] == "california"):
        print("rich mf")
        print(item)
    else:
        print("broke mf ")

##################################
##filter dictionary
#################################
list3 =['guatemala', 'venezuela', 'california']
california_dweller = list(filter(lambda x: True if(x == 'california') else False, list3))
print(california_dweller)


