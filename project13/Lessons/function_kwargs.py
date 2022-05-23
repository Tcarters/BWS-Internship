def thing (name, age=31, *args, **kwargs):
    pass

def person (**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("Your are is ", kwargs.get ("name") )

person(name="Reacher", age=27, brain="Huge")

def order_pizza(name, address, **toppings):
    print(f"Order is for { name} ")
    print (f"Ship it to {address} ")
    price = 18.000

    print ("kwargs ", toppings )

    
    for key , value in toppings.items():
        price = price + 2.00
    print(f"The total price is { price} ")
    return price

order_pizza("Amanda", "Canada", jalapenos=True, extra_cheese=True, ham=True )