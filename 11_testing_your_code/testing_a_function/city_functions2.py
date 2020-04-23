def city_country_population(city,country,population=''):
    if population:
        msg = city.title() + "," + country.title() + '-' + population
    else:
        msg = city.title() + ',' + country.title()
    return msg