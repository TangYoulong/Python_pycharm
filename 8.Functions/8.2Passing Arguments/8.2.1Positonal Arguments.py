def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + "." )
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
#函数可以调用多次
describe_pet('dog','willie')