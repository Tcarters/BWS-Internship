class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

        # print("Rawat ")

    def eat(self):
        print("I am eating some yum yum ...")

    def chase(self, animal="Lion"):
        print (" I am chasing a", animal)
        

class HouseCat (Animal):
    def speak(self):
        print ("Meowwwwwwwwwwww")

    def eat(self):
        super().eat()
        print ("I am eating salmon ")
    
    def chase(self, animal):
        super().chase(animal)
        print (animal, "was caught")

    

cat = HouseCat()
cat.eat()
cat.chase("Gazelle")