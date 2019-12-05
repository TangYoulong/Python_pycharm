def describe_pet(pet_name,animal_type='dog'):
    print(pet_name)
    print(animal_type)
#调用函数
describe_pet('willie')
describe_pet(pet_name='willie')
#调用
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')
