def car_profile(manufacturer,model_number,**other_info):
    car_info = {}
    car_info['manufacturer:'] = manufacturer
    car_info['model_number:'] = model_number
    for key,value in other_info.items():
        car_info[key] = value
    return car_info
#调用函数
information = car_profile('panasonic','number_one',color = 'yellow',price = '1000$')
print(information)

