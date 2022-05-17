sentence = """A sentence in here

"""

def square(func):
    def wrapper(a, b):
        return func(a, b) * func(a, b)
    return wrapper

@square
def add(a, b):
    return a + b

print(add(5, 3))

new = ""
for i in "Hello":
    if i != "l":
        new += I
print (new)