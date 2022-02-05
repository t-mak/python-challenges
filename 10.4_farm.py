class Animal:
    species = "wild animal"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound):
        return f"{self.name} says {sound}"

class Dog(Animal):
    def __init__(self, name, age, race):
        self.race = race
        super().__init__(name, age)
        self.big = True
    
    def animal_weight(self, weight):
        return f"{self.name} weights {weight}"

class Cat(Animal):
    def __init__(self, name, age, claws):
        if (claws == "True" or claws == "False"):
            self.claws = claws
        else:
            print ("claws has to have value of True or False!")
        super().__init__(name, age)
        self.healthy = True
        self.nasty = True
    
    def speak(self, sound="meow"):
        super().speak(sound)

    def has_claws(self):
        if self.claws:
            self.claws = False
            return f"{self.name} has claws! To make it safe, take them away"
        else:
            self.claws = True
            return f"{self.name} has no claws, let's give them back"

class Parrot(Animal):
    def __init__(self, name, age, words):
        self.words = words
        super().__init__(name, age)

    def knowledge(self):
        return f"{self.name} knows {self.words} words"


