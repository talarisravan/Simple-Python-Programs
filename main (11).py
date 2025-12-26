 #Single Inheritance
 class Alpha:
     def fun1(self):
         print("I am an Alpha")
 class Beta(Alpha):
     pass
 b=Beta()
 b.fun1


#Multiple inheritance
 class Alpha:
     def fun1(self):
           print("I am an Alpha")
 class Beta:
     def fun1(self):
         print("I am Beta")
 class Gamma(Alpha,Beta):
     pass
 g=Gamma()
 g.fun1()
        
        
#polymorphism
 class Animal:
     def speak(self):
         print("Animal makes a sound")
 class Dog(Animal):
     def speak(self):
         print("Dog barks")
 class Cat(Animal):
     def speak(self):
         print("Cat meows")
 animals = [Dog(), Cat(), Animal()]
 for a in animals:
     a.speak()

#Abstraction
from abc import ABC, abstractmethod
class Messenger(ABC):
    @abstractmethod
    def send_message(self):
        pass
    @abstractmethod
    def receive_message(self):
        pass
class Fmessage(Messenger):
    def send_message(self):
        print("I am sending message from Facebook")
    def receive_message(self):
        print("I am receiving message from Facebook")
m = Fmessage()
m.send_message()
m.receive_message()

