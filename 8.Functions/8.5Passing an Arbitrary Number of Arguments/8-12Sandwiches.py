def make_sandwich(food_materials):
    for food_material in food_materials:
        info = food_material + " is very nice."
        print(info)
    print("\n")
food_material_0 = ['egg']
food_material_1 = ['egg','beef']
food_matericl_2 = ['egg','beef','greenstuff']
make_sandwich(food_material_0)
make_sandwich(food_material_1)
make_sandwich(food_matericl_2)