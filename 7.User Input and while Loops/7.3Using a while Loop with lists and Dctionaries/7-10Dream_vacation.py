prompt = "\nIf you could visit one place in the world, where would you go? "
places = []
number = 0
while number in range(5):
    place = input(prompt)
    places.append(place)
    number += 1
print(places)
