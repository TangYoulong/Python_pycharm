#创建一个空列表，用来储存外星人
aliens = []
#创建30个外星人
for alien in range(30):
    new_alien = {'color':'white','point':5,'speed':'slow'}
    aliens.append(new_alien)
#显示前6个外星人
for alien in aliens[:6]:
    print(alien)
#显示创建了多少个外星人
print("Total number of aliens:"+str(len(aliens)))
