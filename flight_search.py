import requests
import os

GET_IATA_API_KEY = os.environ.get("GET_IATA_API_KEY")
GET_DEST_CODES_ENDPOINT = os.environ.get("GET_DEST_CODES_ENDPOINT")


class FlightSearch:

    def __init__(self):
        self.destination_code = ""

    def get_destination_code(self, city_name):
        get_iata_params = {
            "term": city_name,
        }
        headers = {
            "apikey": GET_IATA_API_KEY,
        }

        response = requests.get(url=GET_DEST_CODES_ENDPOINT, params=get_iata_params,
                                headers=headers)
        data = response.json()
        self.destination_code = data["locations"][0]["code"]

        return self.destination_code
