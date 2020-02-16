'''假设Car 类有一个名为fill_gas_tank() 的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面演示了一种重写方式：'''
def ElectricCar(Car):
    def fill_gas_tank():
        '''电动汽车没有邮箱'''
        print("This car doesn't need need a gas tank")
'''现在，如果有人对电动汽车调用方法fill_gas_tank() ，Python将忽略Car 类中的方法fill_gas_tank() ，转而运行上述代码。
使用继承时，可让子类保留从父类那里继 承而来的精华，并剔除不需要的糟粕。'''