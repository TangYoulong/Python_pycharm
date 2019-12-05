#many_users.py
users = {
    'aeinstein':{
        'first':'albert',
        'last':'ainstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paries'
    }
}
for username,user_info in users.items():
    print("\nUsername:" + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name:" + full_name.title())
    print("location:" + location)