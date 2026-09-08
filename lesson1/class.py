class Dog:

    kind = "canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    def bark(self):
        print(self.name, "says Woof!")

    def add_trick(self, trick):
        self.tricks.append(trick)
dog1 = Dog("Fido", 3)
dog2 = Dog("Buddy", 5)
dog1.bark()
dog2.bark()
dog1.add_trick("roll over")
dog2.add_trick("play dead")
print(dog1.tricks)
print(dog2.tricks)