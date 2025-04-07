from dataclasses import dataclass

from requests import Response
from requests import get as get_requests
from requests.exceptions import JSONDecodeError

import config
from exceptions import ApiServiceError, CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    """Rounds coordinates to 1 decimal place."""
    if not config.USE_ROUNDED_COORDS:
        return coordinates

    return Coordinates(
        longitude=round(coordinates.longitude, 1),
        latitude=round(coordinates.latitude, 1),
    )


def get_coordinations() -> Coordinates:
    """Returns current coordinations using ipinfo.io API."""
    response: Response = get_requests("https://ipinfo.io/json")

    if response.status_code != 200:
        raise CantGetCoordinates

    try:
        data: dict = response.json()
    except JSONDecodeError:
        raise ApiServiceError

    if "loc" not in data.keys():
        raise CantGetCoordinates

    coordinates: Coordinates = Coordinates(*map(float, data["loc"].split(",")))

    return _round_coordinates(coordinates)


if __name__ == "__main__":
    coordinates = get_coordinations()

    print(f"Latitude: {coordinates.latitude}")
    print(f"Longitude: {coordinates.longitude}")
