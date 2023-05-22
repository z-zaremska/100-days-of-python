import datetime as dt
import requests
import os

USERNAME = os.environ.get('PIXELA_USERNAME')
TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPH_ID = 'first'

# Create new user
pixela_users = 'https://pixe.la/v1/users'

user_parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

new_user = requests.post(url=pixela_users, json=user_parameters)

# Create new graph
pixela_graph = f'{pixela_users}/{USERNAME}/graphs'

graph_parameters = {
    'id': GRAPH_ID,
    'name': 'Coding',
    'color': 'momiji',
    'unit': 'hours',
    'type': 'float',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

new_graph = requests.post(url=pixela_graph, json=graph_parameters, headers=headers)

# Create new pixel
pixela_pixel = f'{pixela_graph}/{GRAPH_ID}'

pixel_parameters = {
    'date': dt.date.today().strftime('%Y%m%d'),
    'quantity': '3'
}

add_pixel = requests.post(url=pixela_pixel, json=pixel_parameters, headers=headers)
