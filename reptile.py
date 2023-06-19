# Showcasing Inheritance

from animal import Animal  #importing Animal class from animal.py file

class Reptile(Animal):

    def __init__(self):
        super().__init__() # initialises the parent / base class - inherit everything from Animal
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles have 4 legs
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None # Not True for all reptiles

    def seek_heat(self):
        print("It's chilly outside, I need a sunbed")
    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("If I have it, may as well use it")

    def attract_mate_through_scent(self):
        print("It's time to put on the aftershave")

bulbasaur = Reptile()

# bulbasaur.hunt() # Hunting Prey
# bulbasaur.breathe() # One breath at ...

