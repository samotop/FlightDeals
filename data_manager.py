import requests
import os

SHEETY_API_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
GET_IATA_API_KEY = os.environ.get("GET_IATA_API_KEY")
PUT_REQ_SHEETY_ENDPOINT = os.environ.get("PUT_REQ_SHEETY_ENDPOINT")
SHEETY_GET_USERS_ENDPOINT = os.environ.get("SHEETY_GET_USERS_ENDPOINT")


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self, object_id, code):
        code_updates = {
            "price": {
                "iataCode": code,
            }
        }
        requests.put(url=f"{PUT_REQ_SHEETY_ENDPOINT}{object_id}", json=code_updates)

    def get_user_data(self):
        response = requests.get(url=SHEETY_GET_USERS_ENDPOINT)
        data = response.json()
        list_of_users = data["users"]
        return list_of_users
