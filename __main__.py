import requests

api_key = '30d98e5f8b3acdf830227a452bddf428'
#input for the target city
city = input('City name: ')
#url for the target city's weather prognosis
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
#response for status codes
res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    temp = data['main']['temp'] - 273.15 
    desc = data['weather'][0]['description']
    print('Temperature: {t} C'.format(t=temp))
    print('Description: {d}'.format(d=desc))
elif res.status_code == 401:
    print('Invalid API key.')
elif res.status_code == 404:
    print('City not found.')
elif res.status_code == 429:
    print('Rate limit exceeded.')
else:
    print('Error getting data: ', res.json())