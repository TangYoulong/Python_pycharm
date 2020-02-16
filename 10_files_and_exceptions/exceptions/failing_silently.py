import os
file_list = os.listdir(r"C:\Users\youlong\PycharmProjects\python入门到实战练习\file_library")
print(file_list)
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
file_normal = ["alice.txt","alice2.txt"]
for file in file_normal:
    filename = r"C:\Users\youlong\PycharmProjects\python入门到实战练习\file_library\\" + file
    count_words(filename)