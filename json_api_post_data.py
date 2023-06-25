import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')

if response.status_code == 200:
    data = response.json()

    for post in data:
        print('Post ID', post['id'])
        print('Title', post['title'])
        print('Body', post['body'])
        print('-----')

else:
    print('Request failed with status code', response.status_code)









