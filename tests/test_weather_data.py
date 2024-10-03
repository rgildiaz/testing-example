# test the WeatherData class

from main import WeatherData
import unittest
from unittest.mock import patch


class TestWeatherData(unittest.TestCase):
    def setUp(self):
        self.mock_api = patch("main.WeatherAPI").start()
        self.weather_data = WeatherData(self.mock_api)

    def tearDown(self):
        patch.stopall()

    def test_get_location_timezone(self):
        """Test WeatherData.get_location_timezone()"""
        # setup
        self.mock_api.get_timezone_from_coordinates.return_value = "TEst"

        # call
        location = (1, 2)
        result = self.weather_data.get_location_timezone(location)

        # test/assertions
        self.mock_api.get_timezone_from_coordinates.assert_called_once_with(1, 2)

        # This will fail because we expected the result to be uppercase, but changed the code to return a lowercase value.
        self.assertEqual(result, "TEST")
