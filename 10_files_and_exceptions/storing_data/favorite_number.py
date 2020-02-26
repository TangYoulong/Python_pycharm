import json

favorite_number = input("please enter your favorite number")
filename = "favorite_number.json"
with open(filename,'w') as f_obj:
    json.dump(favorite_number,f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)




