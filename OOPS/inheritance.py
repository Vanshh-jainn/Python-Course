class Animal:
    Location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Speaking now..")

class Dog(Animal): # this is how inheritance is done in python.
    def speak(self):
        super().speak() #we are using the speak function of parent class
        print("WOOF!")

D = Dog("Tommy")
D.speak()