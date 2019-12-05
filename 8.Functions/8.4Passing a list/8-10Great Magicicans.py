#定义一个打印列表的函数
def show_magicians(change_magicians):
    while change_magicians:
        print(change_magicians)
        break

def make_great(magicians,change_magicians):
    while magicians:
        current = magicians.pop()
        current = "The Great " + current
        change_magicians.append(current)
#定义两个列表，一个为修改前，一个为修改后
magicians = ['magicians1','magicians2']
change_magicians = []
make_great(magicians,change_magicians)
show_magicians(change_magicians)