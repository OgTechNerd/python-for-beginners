nums = [1,2,3,5,6,7,88]

mylist  = [ n*n for n in nums]
print(mylist)
mylist = list(map(lambda n: n*n, nums))
print(mylist)

mylist = [ n for n  in nums if n%2 ==0]
print(mylist)

mylist = list(filter(lambda n: n%2 ==0, nums))
print(mylist)

## lambda functions ##
mx = lambda x,y:x if x >y else y
print(mx(8,5))

## with filter Function ##
n = [45,67,4545,789]
print(list(filter(lambda x: x>1000, n)))
## with map function
n = [4,3,2,1]
print(list(map(lambda x:x**2, n)))
