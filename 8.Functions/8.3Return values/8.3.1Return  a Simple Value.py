#formatted_name.py
def get_formatted_name(first_name,last_name):
    """返回完整的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('Youlong','Tang')
print(musician)