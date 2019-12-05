#按顺序遍历字典中的所有键
#不用sorted反而是顺序的，用了顺序反而不对
favorite_language = {
    'tang':'python',
    'sara':'c',
    'edward':'java',
    'phli':'C++',

}
for name in (favorite_language.keys()):
    print(name.title()+"，thank you for taking the poll")