from abc import ABC, abstractmethod

class AnimalAbstract(ABC):
    @abstractmethod
    def sound(self):
        pass

class DogAbstract(AnimalAbstract):
    def sound(self):
        print("Woof woof!")

class CatAbstract(AnimalAbstract):
    def sound(self):
        print("Meow meow!")

if __name__ == "__main__":
    d = DogAbstract()
    d.sound()