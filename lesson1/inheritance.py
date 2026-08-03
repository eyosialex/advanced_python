class Animal:
    def __init__(self, movement_type, sound):
        self.movement_type = movement_type
        self.sound = sound

    def display(self):
        print(f"Animal Info - Movement: {self.movement_type}, Sound: {self.sound}")

class Dog(Animal):
    def __init__(self, movement_type, sound, breed):
        super().__init__(movement_type, sound)
        self.breed = breed

    def display(self):
        print(f"Dog Info - Breed: {self.breed}, Movement: {self.movement_type}, Sound: {self.sound}")