import requests

class JSONPlaceholderAPI:
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self):
        self.session = requests.Session()

    def get_data(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = self.session.get(url)
        return response.json()

    def display_users(self):
        data = self.get_data('users')
        for item in data:
            print('----------')
            print('Id:', item['id'])
            print('Name:', item['name'])
            print('Email:', item['email'])


    def display_comments(self):
        data = self.get_data('comments')
        for item in data:
            print('----------')
            print('Id: ', item['id'])
            print('Name: ', item['name'])
            print('Email: ', item['email'])
            print('Body', item['body'])


    def display_albums(self):
        data = self.get_data('albums')
        for item in data:
            print('-----------')
            print('Id', item['id'])
            print('Title', item['title'])

    def display_photos(self):
        data = self.get_data('photos')
        for item in data:
            print('----------')
            print('Id: ', item['id'])
            print('Title: ', item['title'])
            print('Url: ', item['url'])
            print('Thumbnail url: ', item['thumbnailUrl'])

    def display_todos(self):
        data = self.get_data('todos')
        for item in data:
            print('----------')
            print('Id: ', item['id'])
            print('Title: ', item['title'])
            print('Completed: ', item['completed'])


api = JSONPlaceholderAPI()
print('Chose and endpoint: 1: users | 2: comments')

input_endpoint = input('Enter an endpoint: ')
if input_endpoint == '1':
    api.display_users()
elif input_endpoint == '2':
    api.display_comments()
elif input_endpoint == '3':
    api.display_albums()
elif input_endpoint == '4':
    api.display_photos()
elif input_endpoint == '5':
    api.display_todos()
else:
    print('Invalid input, Please choose a valid endpoint')
