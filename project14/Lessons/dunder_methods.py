class Animal:
    # fur_color = "Orange"

    animal_type = "Unknown"

    def __init__(self, fur_color) -> None:
        self.fur_color = fur_color
        #pass

    def speak(self):
        raise NotImplementedError

        # print("Rawat ")

    def eat(self):
        print("I am eating some yum yum ...")

    def chase(self, animal="Lion"):
        print (" I am chasing a", animal)
    
    def get_fur_color(self):
        print("Get fur_color is: " ,self.fur_color)
        

class HouseCat (Animal):


    def __init__(self, fur_color) -> None:
        super().__init__(fur_color)
        print("Fur color was saved to the class Object")
        self.animal_type = "House cat"
        print(self.animal_type)

        


        super().__init__(fur_color)
    def speak(self):
        print ("Meowwwwwwwwwwww")

    def eat(self):
        super().eat()
        print ("I am eating salmon ")
    
    def chase(self, animal):
        super().chase(animal)
        print (animal, "was caught")

    
cat = HouseCat("Orange")
cat.get_fur_color()

#cat.chase("mouse")
