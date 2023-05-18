import requests

QUIZ_ENDPOINT = 'https://opentdb.com/api.php'
PARAMETERS = {
    'amount': 10,
    'difficulty': 'easy',
    'type': 'boolean'
}

response = requests.get(url=QUIZ_ENDPOINT, params=PARAMETERS)
question_data = response.json()['results']
