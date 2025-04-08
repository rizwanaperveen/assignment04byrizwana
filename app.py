import requests

from pprint import pprint

API_Key = "b7e3a262b23379304c95fa8f23b8d550"

city = input("Enter the city name: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_Key+ "&q= " + city
weather_data = requests.get(base_url).json()
pprint(weather_data)

