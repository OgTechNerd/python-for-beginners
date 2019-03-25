#from iteration_utilities import duplicates

#result = list(duplicates([44, 55, 66, 44, 55]))
#print(result)
list_of_duplicates = [12, 23, 34, 45, 56, 23, 34]

# converting list to set
# removes duplicates automatically as the set in unique

list_of_nums = list(set(list_of_duplicates))
print(list_of_nums)

def removeDupes(list):
    uninquelist = []
    for elem in list:
        if elem not in uninquelist:
            uninquelist.append(elem)
    
    return uninquelist

newlist = removeDupes([123, 234, 456, 678, 123, 234])
print(newlist)
