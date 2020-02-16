'''导入模块中的所有类'''
'''不推荐使用这种导入方式，其原因有二。首先，如果只要看一下文件开头的import 语句，就能清楚地知道程序使用了哪些类，
将大有裨益；但这种导入方式没有明确地指出你 使用了模块中的哪些类。这种导入方式还可能引发名称方面的困惑。
如果你不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
这里之所以介绍这种导入方式，是因为虽然不推荐使用这种方式，但你可能会在别人编写的代码中见到它。'''
from car_importing_a_single_class import *

my_beetle = Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

