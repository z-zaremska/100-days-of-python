import requests

SHEETY_HEADERS = {'Authorization': 'your_token'}


class UserManager:

    def __init__(self, sheety_token, sheety_url):
        self.sheety_url = sheety_url
        self.sheety_token = sheety_token
        SHEETY_HEADERS['Authorization'] = sheety_token

        print('Welcome to the Flight Club')
        print('We find the best flight prices and e-mail you!')

        want_to_join = input('Do you want to register? (y/n) ')
        if want_to_join.lower() == 'y':
            self.create_new_user()

    def create_new_user(self):
        """Get data from new user and insert it into Users Google Sheet."""
        while True:
            first_name = input('What is your first name? ')
            last_name = input('What is your last name? ')
            email = input('What is your email? ')

            if email == input('Type your email again: '):
                print("You're in the club!")

                user_data = {
                    'user': {
                        'firstName': first_name.upper(),
                        'lastName': last_name.upper(),
                        'email': email.lower()
                    }
                }

                requests.post(url=self.sheety_url, json=user_data, headers=SHEETY_HEADERS)
                break

            else:
                print("Something went wrong.\nLet's try again!")
