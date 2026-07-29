class animal:
     def __init__(self ,move,sound):
        self.move=move
        self.sound=sound
     def move (self,move):
        self.move=move
     def sound(self ,voice):
        self.sound=voice 
class dog (animal):
    def __init__( move, sound,power):
        super().__init__(move, sound)
        self.power=power
    def display(self):
        print ("dog info :",
               self.move,self.sound,self.power)
        