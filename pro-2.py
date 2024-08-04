class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def bark(self):
        print(f"{self.name} Breead Is {self.breed}")
my_dog = Dog("MAX", "Pomeriyan")
my_dog.eat()  
my_dog.bark()
