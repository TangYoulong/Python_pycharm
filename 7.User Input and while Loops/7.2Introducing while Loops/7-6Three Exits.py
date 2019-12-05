#7-6使用Active来控制循环结束的试剂
'''prompt = "\nPlease enter your age"
prompt += "\nEnter 'quit' to end the program"
Active = True
while Active:
    message = input(prompt)
    if message != 'quit':
        age = message
        age = int(age)
        if age <= 12:
            if age > 3:
                price = 10
                price = str(price)
                print("It's " + price + " dollers")
            else:
                print("It's free")
        else:
            price = 15
            price = str(price)
            print("It's " + price + " dollers.")
    else:
        Active = False
'''
#使用break语句在用户输入‘quit’语句时退出循环
active = True
prompt = "\nPlease Enter your age:"
while active:
    message1 = input(prompt)
    if message1 == 'quit':
        print('quit')
        break
    elif int(message1) < 3:
        print("It's free")
    elif  3 <= int(message1) < 12:
        print("It's 10 dollers")
    elif int(message1) >= 12:
        print("It's 15 dollers")