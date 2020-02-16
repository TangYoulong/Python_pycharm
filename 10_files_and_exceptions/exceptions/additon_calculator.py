while True:
    num1 = input("first number:")
    num2 = input("second number:")
    if num1 == "quit":
        break
    if num2 == "quit":
            break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("请输入数字")
    else:
        print(answer)