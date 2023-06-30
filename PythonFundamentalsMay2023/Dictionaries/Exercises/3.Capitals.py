countries_list = [country for country in input().split(", ")]
cities_list = [city for city in input().split(", ")]
dict_countries = dict(zip(countries_list, cities_list))

# for index in range(len(cities_list)):
#     dict_countries.update({countries_list[index]: cities_list[index]})

[print(f"{country_name} -> {city_name}") for country_name, city_name in dict_countries.items()]
