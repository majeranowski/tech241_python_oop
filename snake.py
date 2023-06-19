# Showcasing Encapsulation

from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()

        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None # Not all snakes are venomous
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("Do I say it smells nice, or tastes nice?")

sidney = Snake()
sidney.breathe() # From Animal
sidney.seek_heat() # From Reptiles
sidney.use_tongue_to_smell() # From Snake

# Encapsulation is also really good for protecting important variables/objects

# Types of modifiers in Python -

# Public - Anyone, Anywhere can use it
# Private - Accessible only within the class itself / _<method name>
# Protected - Accessible within the class and it's subclasses / __<method name>


