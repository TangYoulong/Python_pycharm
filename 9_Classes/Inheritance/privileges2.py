'''习题9-12，将Admin和Privileges拆分储存在这个模块中'''
from Inheritance.privileges1 import User

class Admin(User):
    def __init__(self,firstname,lastname,*other_argument):
        super().__init__(firstname,lastname,*other_argument)
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete","can ban user"]

    '''此方法展示管理员权限'''
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)