#! python3
# quickWeather.py - Prints the current weather for a location from the command line.

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
url ='http://openweathermap.org/data/2.5/weather?q=%s,RU&appid=b6907d289e10d714a6e88b30761fae22' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
print(response.text)
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData
print('Current weather in %s:' % location)
print('В %s cейчас ' % (location) + w['weather'][0]['description'])
print()
print('Температура: ' + str(w['main']['temp']))
print()
print('Ветер: ' + str(w['wind']['speed']) + ' метров в сек')

