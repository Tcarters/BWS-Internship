from unicodedata import name


name = "Tdmund"

def function():
    print ( f"Hello {name} ")

def f2 ( name, food ):
    print(f"hello { name}. Let's eat some { food } ")

#def f3 (nom, food="Tacos"):
def exp(num1, num2):
    total = num1 ** num2
    return total

big_number = exp( 12, 4)
print (big_number)
f2('Jon', 'Pizza')

function()