num = input("Enter a numb: ")

try:
    num = int(num)
except ValueError:
    print(num, "was not a valid number...")

except Exception as e:
    print ("Exception wwas caught ")
    print(type(e))

    num =" Unknown"
print (num)

