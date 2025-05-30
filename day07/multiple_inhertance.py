#  first parent class
class Car :
    def __init__(self,brand,model) :
        self.brand = brand
        self.model = model

# 2nd parent class      
class Battery :
    def battery_info(self) :
        return "this is battery"
    

# 3rd parent class
class Engine :
    def engine_info(self) :
        return 'this is 750 H.P. engine'
    

# child class from multiple parent class
class ElectricCar_two(Battery , Engine , Car) :
    pass


my_new_car = ElectricCar_two('tesla' , 'model S')
print(my_new_car.battery_info())
print(my_new_car.engine_info())
