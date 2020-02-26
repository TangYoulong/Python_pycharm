import os
filename = "the_little_prince.txt"
file = r"D:\PycharmProjects\python\file_library\\" + filename
with open(file) as file_object:
    lines = file_object.read()
    the_word = lines.lower().count('a')
print(the_word)