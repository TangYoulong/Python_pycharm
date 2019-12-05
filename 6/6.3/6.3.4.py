favorite_language = {
    'tang':'python',
    'sara':'c',
    'edward':'java',
    'phli':'C++',
    'chen':'c'

}
#使用set可以剔除重复的项目
print("The following language will be mentioned:")
for language in set(favorite_language.values()):
    print(language.title())