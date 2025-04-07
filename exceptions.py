class CantGetCoordinates(Exception):
    """Exception raised when coordinates cannot be obtained."""


class CantGetWeather(Exception):
    """Exception raised when weather cannot be obtained."""


class ApiServiceError(Exception):
    """Exception raised when API service returns an error."""
