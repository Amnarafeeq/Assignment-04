import requests
from pprint import pprint

API_Key = "df19d79415525c66a024eb9adb3edec0"
city = input("Enter a City: ")
base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_Key

weather_data = requests.get(base_url).json()

pprint(weather_data)
