import json
from datetime import datetime
from pathlib import Path
from typing import Protocol, TypedDict

from weather_api_service import Weather
from weather_formatter import format_weather


class WeatherStorage(Protocol):
    """Interface for any storage saving weather data."""

    def save(self, weather: Weather) -> None:
        raise NotImplementedError


class PlainFileWeatherStorage:
    """Storage weather plain in text file"""

    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatter_weather = format_weather(weather)

        with open(self._file, "a", encoding="utf-8") as file:
            file.write(f"{now}\n{formatter_weather}\n")


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage:
    """Storage weather in JSON file"""

    def __init__(self, json_file: Path):
        self._json_file = json_file
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append(
            {"date": str(datetime.now()), "weather": format_weather(weather)}
        )
        self._write(history)

    def _init_storage(self) -> None:
        """Initialize storage if file not exists."""
        if not self._json_file.exists():
            with open(self._json_file, "w", encoding="utf-8") as file:
                file.write("[]")

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._json_file, "r") as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._json_file, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """Saves weather in the storage."""
    storage.save(weather)


if __name__ == "__main__":
    from weather_api_service import WeatherType

    save_weather(
        Weather(
            temperature=25,
            weather_type=WeatherType.CLEAR,
            sunrise=datetime.fromisoformat("2022-05-03 04:00:00"),
            sunset=datetime.fromisoformat("2022-05-03 20:25:00"),
            city="Baku",
        ),
        PlainFileWeatherStorage(Path.cwd() / "history-test.txt"),
    )

    save_weather(
        Weather(
            temperature=25,
            weather_type=WeatherType.CLEAR,
            sunrise=datetime.fromisoformat("2022-05-03 04:00:00"),
            sunset=datetime.fromisoformat("2022-05-03 20:25:00"),
            city="Baku",
        ),
        JSONFileWeatherStorage(Path.cwd() / "history-test.json"),
    )
