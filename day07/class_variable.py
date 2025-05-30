class Car : 

# class_variables
    total_car = 0

    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
        Car.total_car += 1
    
    def get_brand(self) :
        return self.__brand 
    

    def full_name(self) :
        return f"{self.__brand} {self.model}"
    

# object of class Car
my_car = Car("tata" , "safari")

Car('tata' , 'punch')
Car('tata' , 'nexon')


# class variable can acess by class(Car) directly
print(Car.total_car)


# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())
    
# Inheritance class 
class ElectricCar(Car) :
    def __init__(self , brand , model , battery_size) :
        super().__init__(brand , model)
        # self.brand = brand
        # self.model = model
        self.battery_size = battery_size


# object of class ElectricCar
my_tesla = ElectricCar('tesla' , 'model S' , '90kWh')

# print(my_tesla.battery_size)
# print(my_tesla.full_name())
# print(my_tesla.brand)

# brand(object) can only acess by the class method using get_brand
# print(my_tesla.get_brand()) 

# class variable can acess by class(Car) directly
# counting of total car is increase beacuse class ElectricCar will also create an object of class Car
print(Car.total_car)