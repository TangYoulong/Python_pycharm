'''
你还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza 指定别名p ），让你能够更轻松地调用模块中的函数。
相比于pizza.make_pizza() ，p.make_pizza() 更为简洁：
'''
from Importing_an_Entire_Module import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')