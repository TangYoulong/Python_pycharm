class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaruant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaruant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaruant_name + " is open now.")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ["strawberry_flavor","apple_flavor"]

    def show_ice(self):
        for ice in self.flavors:
            print(ice)

IceCreamStand1 = IceCreamStand("HaiDiLao","hot_pot")
IceCreamStand1.show_ice()


