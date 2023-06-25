import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

# check the response status code
if response.status_code == 200:
    try:
        content = response.json()
        for user in content:
            print('User:', user['name'], 'Email:', user['email'])
    except ValueError:
        print('Response content is not a valid JSON')
else:
    print('Request failed with status code:', response.status_code)








