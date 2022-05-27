
class Animal:
    fur_color = "Orange"

    def speak(self):
        print("Rawat ")

    def eat(self):
        pass

    def chase(self):
        pass

calling = Animal()

class Tiger (Animal):
    def speak(self):
        print("They're GREAAAAAATTTT")

class HouseCat (Animal):
    # Overwriting the inner attribute fur_color

    fur_color = "Black"

    def speak(self):
        return "Meow"


#tiger = Animal()
#tiger.speak()
tiger = Tiger()
tiger.speak() # Overwiting the method of Animal class

cat = HouseCat()
print ( cat.speak(),'\n',cat.fur_color)

#print ( type(tiger) )