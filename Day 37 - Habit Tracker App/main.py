import requests
import os

USERNAME = os.environ.get('PIXELA_USERNAME')
TOKEN = os.environ.get('PIXELA_TOKEN')

pixela_users = 'https://pixe.la/v1/users'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Create new user
# new_user = requests.post(url=pixela_users, json=user_parameters)

# Create new graph
pixela_graph = f'{pixela_users}/{USERNAME}/graphs'

graph_parameters = {
    'id': 'first',
    'name': 'Coding',
    'color': 'momiji',
    'unit': 'hours',
    'type': 'float',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

new_graph = requests.post(url=pixela_graph, json=graph_parameters, headers=headers)
print(new_graph)
