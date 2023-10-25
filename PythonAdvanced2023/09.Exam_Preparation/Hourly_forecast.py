def forecast(*cities_info):
    city_forecasts = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }
    result = []

    for city, weather in cities_info:
        if weather in city_forecasts:
            city_forecasts[weather].append(city)

    for weather_forecast, cities in city_forecasts.items():
        [result.append(f"{town} - {weather_forecast}") for town in sorted(cities)]

    return "\n".join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
print()
print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))
print()
print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
