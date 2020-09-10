import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
print(response.status_code)
list1 = ['mia', 'sunny', 'sophie', 'lisa', 'sandra']
dict1 = {"religion": "christian", "feature": "beauty", "profession":"acting"}
dict2 = {"adult": list1, "child": "hermine", "senior": "kate", "character": dict1}
print(dict2)

with open("sample.json", "w") as file:
    filter_list1 = list(filter(lambda x : x.startswith('s'), list1))
    dict3 = {"adult": filter_list1, "child": "hermine", "senior": "kate", "character": dict1}
    json.dump(dict3, file, indent=4)

