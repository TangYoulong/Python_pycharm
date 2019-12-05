prompt = "\nPlease enter your age"
prompt += "\nEnter 'quit' to end the program"
message = input(prompt)
while message != 'quit':
    age = input(prompt)
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
print(message)
