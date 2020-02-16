class User():
    def __init__(self,firstname,lastname,*other_argument):
        self.firstname = firstname
        self.lastname = lastname
        self.other_argument1 = other_argument

    def describe_user(self):

        print("The user's firstname is " + self.firstname)
        print("The user's lastname is " + self.lastname)
        for key in self.other_argument1:
            print("The user's key is " + key)
    def greet_user(self):
        print("Hi " + self.lastname)

class Admin(User):
    def __init__(self,firstname,lastname,*other_argument):
        super().__init__(firstname,lastname,*other_argument)
        self.privileges = ["can add post","can delete","can ban user"]

    '''此方法展示管理员权限'''
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

Admin1 = Admin("Youlong","Tang")
Admin1.show_privileges()
