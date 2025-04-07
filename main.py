from pathlib import Path
from sys import exit
from typing import NoReturn

from coordinates import get_coordinations
from exceptions import ApiServiceError
from history import JSONFileWeatherStorage, PlainFileWeatherStorage, save_weather
from weather_api_service import get_weather
from weather_formatter import format_weather


def main() -> NoReturn:
    try:
        coordinations = get_coordinations()
    except ApiServiceError:
        print("Не смог получить координаты.")
        exit(1)

    try:
        weather = get_weather(coordinations)
    except ApiServiceError:
        print("Не смог получить погоду в API-сервиса погоды.")
        exit(1)

    save_weather(weather, PlainFileWeatherStorage(Path.cwd() / "history.txt"))
    save_weather(weather, JSONFileWeatherStorage(Path.cwd() / "history.json"))
    print(format_weather(weather))
    exit(0)


if __name__ == "__main__":
    main()
