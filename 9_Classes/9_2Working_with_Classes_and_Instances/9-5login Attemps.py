class User():
    def __init__(self,firstname,lastname,*other_argument):
        self.firstname = firstname
        self.lastname = lastname
        self.other_argument1 = other_argument
        self.login_attempts = 0

    def describe_user(self):
        print("The user's firstname is " + self.firstname)
        print("The user's lastname is " + self.lastname)
        for key in self.other_argument1:
            print("The user's key is " + key)
    def greet_user(self):
        print("Hi " + self.lastname)

    '''使属性login_attempts增加1'''
    def increment_login_attempt(self):
        self.login_attempts += 1

    '''方法-重置login_attempts的值为0'''
    def reset_login_attempts(self):
        self.login_attempts = 0

'''定义一个实例'''
User1 = User('Jie','Chen','female','23')
'''调用增加登录属性值的方法'''
User1.increment_login_attempt()
'''打印登录属性值'''
print(str(User1.login_attempts))
'''调用重置属性值的方法'''
User1.reset_login_attempts()
'''打印属性值'''
print(str(User1.login_attempts))