class Battery():

    def __init__(self,battery_size):
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
            range = 0
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

    def check_battery_size(self):
        '''方法-检查电池容量，条件判断，然后修改'''
        if self.battery_size != 85:
            self.battery_size = 85

battery = Battery(80)
battery.get_range()