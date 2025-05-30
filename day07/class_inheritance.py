class Car :
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def get_brand(self) :
        return self.__brand 
    

    def full_name(self) :
        return f"{self.__brand} {self.model}"
    

# my_car = Car("tata" , "safari")
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

my_tesla = ElectricCar('tesla' , 'model S' , '90kWh')

# print(my_tesla.battery_size)
print(my_tesla.full_name())
# print(my_tesla.brand)

# brand(object) can only acess by the class method using get_brand
print(my_tesla.get_brand()) 