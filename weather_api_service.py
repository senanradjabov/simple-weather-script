from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Literal, TypeAlias

from requests import Response
from requests import get as get_requests
from requests.exceptions import JSONDecodeError

import config
from coordinates import Coordinates
from exceptions import ApiServiceError, CantGetWeather

Celsius: TypeAlias = int


class WeatherType(Enum):
    """Weather types."""

    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    """Weather data."""

    temperature: Celsius
    weather_type: WeatherType
    sunrise: datetime
    sunset: datetime
    city: str


def get_weather(coordination: Coordinates) -> Weather:
    """Returns current weather using OpenWeatherMap API."""
    openweather_data: dict = _get_openweather_data(
        coordination.latitude, coordination.longitude
    )
    weather: Weather = _parse_openweather_data(openweather_data)

    return weather


def _get_openweather_data(latitude: float, longitude: float) -> dict:
    response: Response = get_requests(
        config.OPENWEATHER_URL.format(latitude=latitude, longitude=longitude)
    )

    if response.status_code != 200:
        raise CantGetWeather

    try:
        data = response.json()
    except JSONDecodeError:
        raise ApiServiceError

    return data


def _parse_openweather_data(openweather_dict: dict) -> Weather:
    return Weather(
        temperature=_parse_temperature(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, "sunrise"),
        sunset=_parse_sun_time(openweather_dict, "sunset"),
        city=_parse_city(openweather_dict),
    )


def _parse_temperature(openweather_dict: dict) -> Celsius:
    return openweather_dict["main"]["temp"]


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError

    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS,
    }

    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type

    raise ApiServiceError


def _parse_sun_time(
    openweather_dict: dict, time: Literal["sunrise"] | Literal["sunset"]
) -> datetime:
    return datetime.fromtimestamp(openweather_dict["sys"][time])


def _parse_city(openweather_dict: dict) -> str:
    return openweather_dict["name"]


if __name__ == "__main__":
    print(get_weather(Coordinates(40.4, 49.9)))
