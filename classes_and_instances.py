# # Classes
#
# #creating a class - this is like a template
#
# class Dog:  #capitalize letter
#     animal_kind = "canine" #class variable
#
#     def bark(self): #class function = methods  self - referring to a current class.
#         self.animal_kind
#         return "woof"
#
# print(Dog.animal_kind) #canine
# print(Dog.bark(Dog)) #woof
#
# # Instantiation of a class
#
# fido = Dog()
# lassie = Dog()
#
# print(type(fido)) # <class '__main__.Dog'>
# print(type(lassie)) # <class '__main__.Dog'>
# print(fido.bark()) # bark
# print(lassie.animal_kind) # canine
#
# # class variables can be overwritten
# fido.animal_kind = "Big Dog"
# print(fido.animal_kind) # Big Dog  - you can overwrite class attribute per class instance in the object
#
# # Be careful of class variables
#
# Dog.animal_kind = "Dolphin"
# print(lassie.animal_kind) #Dolphin
# print(fido.animal_kind) # Big Dog - still
#
# # Be careful of the scope of the classes





