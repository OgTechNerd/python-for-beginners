#!/usr/bin/python

from  string import Template

def SimpleCart():
    cart = []
    expense = 0
    cart.append(dict(item='coke', price=10, qty=2))
    cart.append(dict(item='cake', price=12, qty=11))
    cart.append(dict(item='biscuit', price=15, qty=7))
    t = Template('$qty x $price = $item')
    for data in cart:
        print(t.substitute(data))
        data["item_price"] = (data["price"] * data["qty"])
        print("Total: "+ str(data["item_price"]))
        expense += int(data["item_price"])
    print("All Expenditure : {}".format(expense))


def ComplexShoppingCart(cart):
    temp = Template('$price * $quantity * ($discount/100)')
    for key ,value in cart.items():
        print(temp.substitute(value))
        cart[key]['cost'] = (int(cart[key]['price']) * int(cart[key]['quantity']) - (int(cart[key]['price']) * int(cart[key]['quantity']) * (int(cart[key]['discount'])/100)))
        #print("Actual Cost {}".format(str(cart[key]['cost'])))
        print("Total Cost: {0} for person {1}".format(str(cart[key]['cost']), key))

if __name__ == '__main__': 
    #Main()
    cart_dict={
        'shaun': {'product': 'budweiser', 'price': '285', 'quantity': '120' , 'discount': '5'},
        'linda': {'product': 'coffee', 'price': '45', 'quantity': '50', 'discount': '8'},
        'Jessica': {'product': 'milk', 'price': '20', 'quantity': '170', 'discount': '7'}
    }
    SimpleCart()
    ComplexShoppingCart(cart_dict)