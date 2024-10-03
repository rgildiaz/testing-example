import openmeteo_requests


class WeatherAPI:
    def __init__(self):
        self.om = openmeteo_requests.Client()

    def get_from_coordinates(self, latitude: float, longitude: float):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
            "current": ["temperature_2m", "relative_humidity_2m"]
        }

        responses = self.om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
        return responses[0]

    def get_timezone_from_coordinates(self, latitude: float, longitude: float) -> str:
        """Get the timezone"""
        response = self.get_from_coordinates(latitude, longitude)
        return response.Timezone()


class WeatherData:
    def __init__(self,  api: WeatherAPI = None):
        self.api = api or WeatherAPI()

    def get_location_timezone(self, location: tuple[float, float]):
        lat = location[0]
        long = location[1]
        timezone = self.api.get_timezone_from_coordinates(lat, long)

        # return the timezone in lowercase
        return timezone.lower()


if __name__ == "__main__":
    locations_to_fetch = [
        (48.8566, 2.3522),  # Paris
        (51.5074, 0.1278),  # London
        (40.7128, -74.0060),  # New York
    ]
    weather_data = WeatherData()

    for location in locations_to_fetch:
        timezone = weather_data.get_location_timezone(location)
        print(f"Timezone for {location} is {timezone}")
