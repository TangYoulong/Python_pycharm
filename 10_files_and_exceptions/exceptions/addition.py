num1 = input("please input first num:")
num2 = input("please input second num:")
try:
    num1Int = int(num1)
    num2Int = int(num2)
except TypeError:
    print("只能输入数字")
else:
    print(num1Int+num2Int)
