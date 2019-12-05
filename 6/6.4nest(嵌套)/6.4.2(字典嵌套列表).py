#pizza.py
'''pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}
#介绍所点的披萨
print("You ordered a " +pizza['crust'] + "-crust pizza" + " with the following toppings:" )
for topping in pizza ['toppings']:
    print("\t" + topping) '''
#favorite_language.py
favorite_language = {
    'tang':['python','python'],
    'sara':['c','python'],
    'edward':['java','python'],
    'phli':['C++','python']
}
for name,languages in favorite_language.items():
    print("\n" + name.title() + " 's favorite languages are:")
    for language in languages:
        print("\t" + language.title())