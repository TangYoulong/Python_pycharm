filename = 'programming_poll.txt'
with open(filename,'a') as fileobject:
    while True:
        msg = input('Please enter your reasons of liking programming:')
        if msg == 'quit':
            break
        else:
            fileobject.write(msg + '\n')