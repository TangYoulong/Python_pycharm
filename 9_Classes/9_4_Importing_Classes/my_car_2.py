'''从一个模块中导入多个类'''
from car_importing_a_single_class import Car,ElectricCar

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
