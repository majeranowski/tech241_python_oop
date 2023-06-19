# Showcasing Polymorphism

from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")
    def constrict(self):
        print("and ....squeeeeeze")

    def climb(self):
        print("up we go")

    def breathe(self):
        print("I am breathing but I am a Python")

peter = Python()

peter.breathe() # method from Python class
peter.eat() # method from Animal class
peter.hunt() # method from Reptile hunt
peter.use_tongue_to_smell() # method from Snake class
