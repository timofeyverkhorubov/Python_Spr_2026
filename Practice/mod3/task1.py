import requests

city = input("Введите название города: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "units": "metric",
    "lang": "ru",
    "appid": "79d1ca96933b0328e1c7e3e7a26cb347"
}

data = requests.get(url, params=params).json()

if data.get("cod") != 200:
    print("Ошибка:", data.get("message", "Город не найден"))
else:
    main = data["main"]
    wind = data["wind"]
    weather = data["weather"][0]

    temp = round(main["temp"])
    feels_like = round(main["feels_like"])
    wind_speed = wind["speed"]
    wind_deg = wind["deg"]
    pressure = round(main["pressure"] * 0.750062)
    humidity = main["humidity"]
    description = weather["description"]

    # Направление ветра (4 стороны)
    if wind_deg < 45 or wind_deg >= 315:
        wind_dir = "северный"
    elif wind_deg < 135:
        wind_dir = "восточный"
    elif wind_deg < 225:
        wind_dir = "южный"
    else:
        wind_dir = "западный"

    print(f"\nПогода в городе {city}:")
    print(f"Температура: {temp}°C")
    print(f"Ощущается как: {feels_like}°C")
    print(f"Ветер: {wind_speed} м/с, {wind_dir}")
    print(f"Давление: {pressure} мм рт. ст.")
    print(f"Влажность: {humidity}%")
    print(f"Небо: {description}")