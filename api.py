# import libraries
import requests

# api key for open weather api
API_KEY = 'b4eae007caa0b7facdf7fe531ebb8d88'


# this class is responsible for making API calls to Open Weather Map's Weather API
class ApiCaller:

    def __init__(self, loc):
        self.loc = loc
        self.coordinates_data = ""
        self.weather_data = self.get_weather_data(loc)
        if self.coordinates_data:
            self.location_string = f'{self.coordinates_data[0]["name"]}, {self.coordinates_data[0]["state"]}'
            self.temp_converted_to_c = round(self.weather_data["current"]["temp"] - 273.15)
            self.icon_code = self.weather_data["current"]["weather"][0]["icon"]
            self.icon_url = 'https://openweathermap.org/img/wn/' + self.icon_code + '@2x.png'

    def get_weather_data(self, place):
        coordinates_url = \
            f'http://api.openweathermap.org/geo/1.0/direct?q={place},{"."},{"GB"}&limit=5&appid={API_KEY}'
        coordinates_response = requests.get(coordinates_url)
        self.coordinates_data = coordinates_response.json()
        if coordinates_response.status_code == 200 and len(self.coordinates_data) != 0:
            latitude = self.coordinates_data[0]['lat']
            longitude = self.coordinates_data[0]['lon']

            # request data matching for matching latitude and longitude from open weather onecall api
            weather_url = f'https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid={API_KEY}'
            weather_response = requests.get(weather_url)
            weather_data = weather_response.json()

            return weather_data






