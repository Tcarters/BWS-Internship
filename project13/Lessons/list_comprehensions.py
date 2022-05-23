from sympy import numer


numbers = []

for num in [1, 2, 34, 89, 0, 3]:
    numbers.append(num**2)
print(numbers)

n2 = [ num**2 for num in [1, 2, 3, 45, 90]]

print(n2)

