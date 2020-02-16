user = input("please enter your name:")
filename = 'guest.txt'
with open(filename,'a') as file_object:
    file_object.write(user + "\n")