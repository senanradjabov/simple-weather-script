from os import getenv

USE_ROUNDED_COORDS: bool = True
OPENWEATHER_API: str | None = getenv("OPENWEATHER_API")
OPENWEATHER_URL: str = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    f"appid={OPENWEATHER_API}&lang=ru&"
    "units=metric"
)

if OPENWEATHER_API is None:
    raise ValueError("OPENWEATHER_API must be set in environment variables")
