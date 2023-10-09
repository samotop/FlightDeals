import requests
import os

SHEETY_POST_USERS_ENDPOINT = os.environ.get("SHEETY_POST_USERS_ENDPOINT")


class UsersManager:
    def __init__(self, user_first_name, user_last_name, user_email):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_email = user_email

    def register_new_member(self):
        user_data = {
            "user": {
                "firstName": self.user_first_name,
                "lastName": self.user_last_name,
                "email": self.user_email,
            }
        }

        requests.post(url= SHEETY_POST_USERS_ENDPOINT, json=user_data)







