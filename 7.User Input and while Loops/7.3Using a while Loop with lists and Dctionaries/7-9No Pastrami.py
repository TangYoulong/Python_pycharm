sandwich_orders = ['sandwich1','sanwich2','sandwich3','Pastrami','Pastrami','Pastrami']
print("熟食店的五香牛肉卖完了")
print(sandwich_orders)
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print(sandwich_orders)