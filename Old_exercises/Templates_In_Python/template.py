#!/usr/bin/python

from  string import Template

def Main():
    cart = []
    cart.append(dict(item='coke', price=10, qty=2))
    cart.append(dict(item='cake', price=12, qty=11))
    cart.append(dict(item='bichi', price=15, qty=7))
    print(cart)
    t = Template('$qty x $price = $item ')
    total = 0 
    print("cart:")
    for data in cart:
         print(t.substitute(data))
         data["Item_Price"] = (data["price"] * data["qty"])
         print("Total: "+ str(data["Item_Price"]))
         expense =+ data["Item_Price"]
    print("All Expenditure : {}".format(expense))
    print(cart)


if __name__ == '__main__': 
    Main()