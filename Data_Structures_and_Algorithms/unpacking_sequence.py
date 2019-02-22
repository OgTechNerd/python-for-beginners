#!/usr/local/bin python
# Any sequence can be packed into variables using simple
# assignment. The only requirement is that the number of 
# variables and structure match the seq
import heapq


data = ['Acme', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print("name: {0} shares {1} price {2} date {3}".format(name, shares, price, date))
items = [1, 10 ,7, 4, 5, 9]

#Finding the largest o Smallest N items.
nums = [1, 8, 2, 23, 77, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# if you are looking for the N smallest or Largest items and N is small
# compared to the overall size  of the collection these functions provide
# performance. 


nums = [1, 8, 2, 23,  7, -4, 18, 23, 42]
import heapq
heap = list(nums)
heapq.heapify(heap)
print(heap)
portfolio = [ 
    {'name': 'IBM', 'shares':100, 'price': 91.1},
    {'name': 'ACME', 'shares': 75, 'price': 115.65},
    {'name': 'BANERG', 'shares': 100, 'price': 212}
    ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)