import json

'''获取储存的用户名'''
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    filename = 'username.json'
    username = input("what's your name?")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        return username

def greet_user():
    username = get_stored_username()
    confirm = input("Is " + username + " your name?,if it is ,please enter 'yes';otherwise enter 'no'")
    if confirm == 'yes':
        print("wellcome back " + username + "!")
    else:
        username = get_new_username()
        print("we'll remember you when you comeback " + username + "!")

greet_user()