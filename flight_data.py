import requests
import datetime
import os

KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_SEARCH_ENDPOINT = os.environ.get("KIWI_SEARCH_ENDPOINT")

today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(1)
tomorrow_date = tomorrow.strftime("%d/%m/%Y")

half_year = today + datetime.timedelta(182)
half_year_date = half_year.strftime("%d/%m/%Y")


class FlightData:
    def __init__(self):
        self.flights_found = False

    def get_fly_data(self, city, lowest_price):
        headers = {
            "apikey": KIWI_API_KEY
        }
        fly_details = {
            "fly_from": "BUD",
            "fly_to": city,
            "date_from": tomorrow_date,
            "date_to": half_year_date,
            "price_to": lowest_price,
            "limit": 100,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "max_stopovers": 4,
        }

        response = requests.get(url=KIWI_SEARCH_ENDPOINT, headers=headers, params=fly_details)
        formatted_response = response.json()

        try:
            if len(formatted_response["data"]) > 0:
                self.flights_found = True

        except KeyError:
            pass

        return formatted_response
