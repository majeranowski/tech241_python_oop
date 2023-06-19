# OOP

Object orientated programming 

By creating classes we can create unique instances of objects with specific methods.

![classes](MicrosoftTeams-image%20(8).png)

```python
#creating a class - this is like a template

class Dog:  #capitalize letter
    animal_kind = "canine" #class variable

    def bark(self): #class function = methods  self - referring to a current class.
        self.animal_kind
        return "woof"

print(Dog.animal_kind) #canine
print(Dog.bark(Dog)) #woof
```

# Initiations 

```python
# Instantiation of a class

fido = Dog()
lassie = Dog()

print(type(fido)) # <class '__main__.Dog'>
print(type(lassie)) # <class '__main__.Dog'>
print(fido.bark()) # bark
print(lassie.animal_kind) # canine

# class variables can be overwritten
fido.animal_kind = "Big Dog"
print(fido.animal_kind) # Big Dog  - you can overwrite class attribute per class instance in the object

# Be careful of class variables

Dog.animal_kind = "Dolphin"
print(lassie.animal_kind) #Dolphin
print(fido.animal_kind) # Big Dog - still

# Be careful of the scope of the classes


```


![classes](MicrosoftTeams-image%20(9).png)

![classes](MicrosoftTeams-image%20(10).png)

### 4 pillars of OOP

* Encapsulation - > Classes are self contained. 
* Abstraction - > simple solution of more complex problem. You don't always need to know how something works to use it.
* Inheritance - > You can create the class that takes variables and class methods from the parent class
* Polymorphism - > Methods can have the same name, but act differently

### Abstraction

```python
# Animal class

class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath at a time, in and out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("Onwards and upwards")

# breathe is abstracted. You can use it without knowing how it works
cat = Animal()
# cat.breathe()
```

### Inheritance

```python
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

```
### Encapsulation


```python
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



```

### Polymorphism

```python
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

```

![Animal-snakes-classes](MicrosoftTeams-image%20(12).png)
# tech241_python_oop
