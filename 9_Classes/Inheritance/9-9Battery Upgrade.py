class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    '''定义一个用于描述的方法'''
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

'''定义一个电池的类（相当于从ElectricCar中拆分出来）'''
class Battery():

    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        '''打印一条消息，指出电瓶的续航里程'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        else:
            range = "Don't know "
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

    def check_battery_size(self):
        '''方法-检查电池容量，条件判断，然后修改'''
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery(80)

ElectricCar1= ElectricCar('tesla','model s',2016)
ElectricCar1.battery.get_range()
ElectricCar1.battery.check_battery_size()
ElectricCar1.battery.get_range()