"""Формирование URL запроса погоды (исправленный код, задание 1878)."""

API_URL = "http://api.example.com/weather"


def get_weather_url(city, days):
    """Собирает URL запроса погоды для города на заданное число дней."""
    full_url = API_URL + "?city=" + city + "&days=" + str(days)
    print("Запрос погоды:", full_url)
    return full_url


if __name__ == "__main__":
    url = get_weather_url("Казань", 3)
