# class MyClass :
#     x = 5
#     y = 23
#     z = x + y

# C1 = MyClass()
# print(C1.x,'+',C1.y,'=',C1.z)


class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age 

    def __str__(self):
        return f"{self.name},({self.age})" 
    
    
    
p1 = Person('john_wick','45')
print(p1)
print('name == ',p1.name)
print('age == ',p1.age)