'''导入整个模块'''
'''这里因为模块名过长，定义了一个别名，为car'''
import car_importing_a_single_class as car

my_beetle = car.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())