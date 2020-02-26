import os
file_list = os.listdir(r"D:\PycharmProjects\python\file_library")
file_names = ["cat.txt","dog.txt","1.txt"]
for filename in file_names:
    file = r"D:\PycharmProjects\python\file_library\\" + filename
    try:
        with open(file) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)