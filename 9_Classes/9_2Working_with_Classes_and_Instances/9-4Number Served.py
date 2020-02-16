class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number = 0

    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaruant_name + " is open now.")

    '''记录在餐馆就餐过的人数'''
    def number_served(self):
        print(str(self.number))

    '''定义设置就餐人数的方法'''
    def set_number_served(self,update_number):
        self.number = update_number

    '''定义递增就餐人数的方法'''
    def increment_number_served(self,increment_number):
        self.number += increment_number

'''实例化类'''
Restaurant_1 = Restaurant('Hai_Di_Lao','hot_pot')
'''打印实例的属性值'''
print(Restaurant_1.restaruant_name)
print(Restaurant_1.cuisine_type)
'''调用实例的方法,描述餐馆'''
Restaurant_1.describe_restaurant()
'''调用实例的方法，打印餐馆正在营业'''
Restaurant_1.open_restaurant()
'''调用实例的方法，打印在餐馆就餐的人数'''
Restaurant_1.number_served()
'''调用实例的方法，打印设置的在餐馆就餐的人数'''
Restaurant_1.set_number_served(100)
Restaurant_1.number_served()
'''调用实例的方法，增加在餐馆中就餐的人数,并打印'''
Restaurant_1.increment_number_served(100)
Restaurant_1.number_served()
