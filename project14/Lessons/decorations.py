def myfunct():
    print("My name is Tc")

#@decorator
# myfunct()


def my_decoration(funct):
    def wrapper():
        print("Do something here")
        funct()
        print("Original function is finished ")
    return wrapper

@my_decoration
def myfunct2():
    print("Second function ...")

myfunct2()
#new_func = my_decoration(myfunct)
#new_func()

# Method 2
