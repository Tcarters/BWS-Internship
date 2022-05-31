class Animal:
    fur_color = "Orange"

    def speak(self):
        raise NotImplementedError

        # print("Rawat ")

    def eat(self):
        pass

    def chase(self):
        pass
class HouseCat (Animal):
    def speak(self):
        print ("Meowwwwwwwwwwww")
    

cat = HouseCat()
cat.speak()
