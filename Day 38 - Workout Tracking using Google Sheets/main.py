import requests
import os
import datetime as dt

NIUTRITIONIX_API_KEY = os.environ.get('NIUTRITIONIX_API_KEY')
NIUTRITIONIX_API_ID = os.environ.get('NIUTRITIONIX_API_ID')
NIUTRITIONIX_USERNAME = os.environ.get('NIUTRITIONIX_USERNAME')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
today = dt.date.today().strftime('%d/%m/%Y')
now = dt.datetime.now().strftime('%X')


nutri_headers = {
    'x-app-id': NIUTRITIONIX_API_ID,
    'x-app-key': NIUTRITIONIX_API_KEY
}

exercises = input('Tell me which exercises you did: ')

natural_exercise_input = {
    "query": exercises,
    "gender": "female",
    "weight_kg": os.environ.get('MY_WEIGHT'),
    "height_cm": os.environ.get('MY_HEIGHT'),
    "age": 30
}

niutritionix_natural_exercise = 'https://trackapi.nutritionix.com/v2/natural/exercise'
activity_response = requests.post(url=niutritionix_natural_exercise, json=natural_exercise_input, headers=nutri_headers)
activity_response.raise_for_status()
activity_data = activity_response.json()['exercises']
print(activity_data)

sheet_url = 'https://api.sheety.co/3940615f01c64bc132046d75bfe21c84/myWorkouts/workouts'

for activity in activity_data:
    exercise_data = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": activity["name"].title(),
            "duration": activity["duration_min"],
            "calories": activity["nf_calories"]
        }
    }

    sheety_headers = {'Authorization': SHEETY_TOKEN}

    insert_activity = requests.post(url=sheet_url, json=exercise_data, headers=sheety_headers)
