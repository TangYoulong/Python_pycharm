filename = '1.txt'
try:
    with open(filename) as fileobject:
        content = fileobject.read()
except FileNotFoundError:
    msg = "Sorry,the file " + filename + " does not exist."
    print(msg)