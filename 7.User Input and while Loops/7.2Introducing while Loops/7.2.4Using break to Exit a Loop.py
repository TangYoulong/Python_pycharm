#要立即退出while 循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break 语句。
#cities.py
prompt = "\nPlease enter the name of a city you have visited:"
prompt +="\nEnter quit when you are finished."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")