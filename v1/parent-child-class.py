
class Entity():
  def __init__(self, isEntity):
    self.isEntity = isEntity

class LivingThing(Entity):
  def __init__(self, isLive, isEntity):
    self.isLive = isLive
    self.isEntity = isEntity

  def isLiving(self):
      if self.isLive == 1:
        print("I am living")
      elif self.isLive == 0:
        print("....")

class Animal(LivingThing):
  def __init__(self,isLive,isEntity, name, age, realm):
    self.name = name
    self.age = age
    self.realm = realm
    self.isLive = isLive
    self.isEntity= isEntity

class Dog(Animal):
  def __init__(self,isLive, isEntity, name, age, realm):
    self.isLive = isLive
    self.isEntity = isEntity
    self.name = name
    self.age = age
    self.realm = realm
    self.type = "dog"

  def speakDog(self):
    if self.isEntity and self.isLive:
      print(f"My name is {self.name}, and I am Living Entity and {self.realm}. My age is {self.age}, my type is {self.type}")

myAnimal = Dog(True, True,'Gofret', 5, 'Animal')
myAnimal.speakDog()
myAnimal.isLiving()
