import json

import requests

def get_weather(city):
    api_key = 'e1ca9fe4899234e124c44c95680caa69'


    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f'Weathre in {city}: Temperature: {temperature}°C, Desrciption: {description}')
    else:
        print('Request failed with status code:', response.status_code)

get_weather('Trinec')