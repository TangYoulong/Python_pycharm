def guest_book():
    filename = 'guest_book.txt'
    with open(filename,'a') as file_object:
        while True:
            user = input("please enter your name:")
            if user == 'quit':
                break
            else:
                file_object.write(user + "\n")
                print("Hello " + user)
                continue

guest_book()



