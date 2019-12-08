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

User1 = User('Jie','Chen','female','23')
User1.describe_user()
User1.greet_user()

User2 = User('Jie','Lv','male','23')
User2.describe_user()
User2.greet_user()