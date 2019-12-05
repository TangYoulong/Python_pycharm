#有时候，需要让实参变成可选的
'''def get_formatted_name(first,middle,last_name):
    """返回完整的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
musician = get_formatted_name('join','lee','hooker')
print(musician)'''
def get_formatted_name(first_name,last_name,middle_name=''):
    """返回完整的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('Youlong','Tang')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)