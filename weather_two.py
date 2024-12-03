import requests

url = 'https://api.weatherapi.com/v1/current.json?key=321ed96661534610b9f14235240312&q=Adelaide&aqi=no'

response = requests.get(url)
weather_json = response.json()

print(weather_json)
