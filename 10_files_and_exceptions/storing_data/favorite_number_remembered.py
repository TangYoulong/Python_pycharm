import json

filename = "favorite_number.json"
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
except FileNotFoundError:
    favorite_number = input("please input your favorite number")
    with open(filename,'w') as f_obj:
        json.dump(favorite_number,f_obj)
else:
    print("your favorite number is " + favorite_number + "!")
