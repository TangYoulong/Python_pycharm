def get_formatted_name(first,last,middle=''):
    '''middle中间名为可选'''
    if middle:
        full_name = first + ' ' + middle + ' '  + last
    else:
        full_name = first + ' ' + last
    return full_name.title()