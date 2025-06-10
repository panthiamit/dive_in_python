# class Customer() :
#     def __init__(self,name):
#         self.name = name
    

# def greet(customer):
#     print('Hello',customer.name)

# cust = Customer('Amit')

# greet(cust)


class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.speak() 
