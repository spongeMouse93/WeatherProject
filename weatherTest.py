import requests

APIKEY = "a0d41aebf4d1481c89862c06701c4e1e"
url = 'https://api.weatherbit.io/v2.0/current'

def CtoF(temp):
  return temp * 1.8 + 32
  
def getWeather(city):
  params = {
    'key': APIKEY,
    'city': city
  }
  response = requests.get(url, params = params)
  if response.status_code != 200:
    print("Error")
  else:
    data = response.json()
    weather_data = data['data'][0]
    temp = CtoF(weather_data['temp'])
    description = weather_data['weather']['description']
    wind_speed = weather_data['wind_spd']
    humidity = weather_data['rh']
    print(f"Temperature: {temp}°F")
    print(f"Description: {description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Humidity: {humidity}%")
   
city = input("Enter city name: ")
getWeather(city)
