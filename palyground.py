import requests
import json

input_endpoint = input('enter an endpoint: ')
response = requests.get('https://jsonplaceholder.typicode.com/comments')

data = response.json()

if response.status_code == 200:
    # print(json.dumps(data, indent=4))
    print(f'The status code =  {response.status_code}')

else:
    print(f'Request failed with {response.status_code}')

for item in data:
    print('-------')
    print('item ID is:', item['id'])
    print('Name:', item['name'])
    print('Email: ', item['email'])
    print('---------')