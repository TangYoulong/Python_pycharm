'''创建一个模拟小狗的类'''
'''函数之间最好要间隔一行，以便区分'''
class Dog():
    def __init__(self,name,age):
        '''初始化属性name和age'''
        self.name = name
        self.age = age

    def sit(self):
        '''模拟小狗被命令时蹲下'''
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        '''模拟小狗被命令时打滚'''
        print(self.name.title() + " rolled over!")
'''实例化类'''
my_dog = Dog('while',6)
print("My dog's name is" + my_dog.name.title() + ".")

my_dog.sit()
my_dog.roll_over()
