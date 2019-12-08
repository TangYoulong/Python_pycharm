'''
如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别别名名 ——函数的另一个名称，
类似于外号。要给函数指定这种特殊外 号，需要在导入它时这样做。
通用语法-from module_name import function_name as fn
'''
from Importing_an_Entire_Module.pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green peppers','extra cheese')