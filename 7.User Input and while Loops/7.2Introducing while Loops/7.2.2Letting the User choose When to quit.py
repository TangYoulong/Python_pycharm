#parrot.py
prompt = "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
#因为'quit'也作为一条信息打印，所以添加一条if语句(实际没有作用，具体原因？)
    #if message != 'quit':
        #print(message)