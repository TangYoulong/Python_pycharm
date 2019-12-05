favorite_places ={
    'Youlong Tang':['Shanghai','Guangzhou','NewYork'],
    'Jie Chen':['Shanghai','NewYork','Beijing'],
    'Dean':['Beijing','Shanghai','Tokyo']
}
for name,favorite_place in favorite_places.items():
    print(name)
    print(favorite_place)
    for places in favorite_place:
        print(places)