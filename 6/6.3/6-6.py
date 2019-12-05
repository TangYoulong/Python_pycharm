#用key.()方法遍历字典
favorite_language = {
    'tang':'python',
    'sara':'c',
    'edward':'java',
    'phli':'C++',

}
'''friends = ['sara','phli']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("hi"+name.title()+",i see your favorite language is "+favorite_language[name].title()+"!")'''
survey = ['sara','edward']
for name in favorite_language.keys():
    if name in survey:
        print( name+" thanks for the survey")
    else:
        print(name+" Please participate in the survey")