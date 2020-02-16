class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaruant_name + " is open now.")
'''第一个实例'''
Restaurant1 = Restaurant('Hai_Di_Lao_1','Hot_pot_1')
Restaurant1.describe_restaurant()

'''第二个实例'''
Restaurant2 = Restaurant('Hai_Di_Lao_2','Hot_pot_2')
Restaurant2.describe_restaurant()

'''第三个实例'''
Restaurant2 = Restaurant('Hai_Di_Lao_2','Hot_pot_2')
Restaurant2.describe_restaurant()