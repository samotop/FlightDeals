from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from users_manager import UsersManager

print("Welcome to Flight Club!\nWe will find the best flight deals and email you.")
first_name = input("What is your first name?")
last_name = input("What is your last name?")

#EMAIL VALIDATION
validation = False
while not validation:
    email_first_time = input("What is your email? ")
    email_second_time = input("Type your email again. \n")
    if email_first_time == email_second_time:
        user_email = email_first_time
        validation = True
    else:
        print("Validation failed. Try again.")
print("Welcome to the Flight Club!")

#CREATE USER / PUT REQUEST TO SHEETY
users_manager = UsersManager(user_first_name=first_name, user_last_name=last_name,
                             user_email= email_first_time )
users_manager.register_new_member()

#GET DATA FROM SHEETY GOOGLE SHEETS
data_manager = DataManager()
data_manager.get_destination_data()


#ADD IATA CODES TO CITIES IN GOOGLE SHEETS
flight_search = FlightSearch()
for data in data_manager.get_destination_data():
    code = flight_search.get_destination_code(data["city"])
    if data["iataCode"] == "":
        data_manager.update_destination_codes(object_id=data["id"], code=code)

#LOOP THROUGH GOOGLE SHEETS DATA AND FIND DATA BASED ON CITY CODE AND LOWEST PRICE
for data in data_manager.get_destination_data():
    lowest_price = data["lowestPrice"]
    destination_code = data["iataCode"]
    flight_data = FlightData()
    formatted_flight_data = flight_data.get_fly_data(destination_code, lowest_price)
    #CHECK IF THERE ARE ANY FLIGHTS FOR THIS ROW ON SHEETY/SET THE RELEVANT VARIABLES
    if flight_data.flights_found:
        flight_price = formatted_flight_data["data"][0]["price"]
        city_from = formatted_flight_data["data"][0]["cityFrom"]
        city_to = formatted_flight_data["data"][0]["cityTo"]
        from_iata = formatted_flight_data["data"][0]["cityCodeFrom"]
        to_iata = formatted_flight_data["data"][0]["cityCodeTo"]
        start_date = formatted_flight_data["data"][0]["local_departure"]
        formatted_start_date = start_date.split("T")
        start_date = formatted_start_date[0]
        link_for_book = formatted_flight_data["data"][0]["deep_link"]
        #LOOP TROUGH FLIGHT AND FIND DATE OF DEPARTURE
        for route in formatted_flight_data["data"][0]["route"]:
            if route["cityCodeFrom"] == to_iata:
                finish_date = route["local_departure"]
                formated_finish_date = finish_date.split("T")
                finish_date = formated_finish_date[0]
        #CREATE TEXT FOR MESSAGE
        text_message = f"Pozor! Nízka cena letenky! Len {flight_price}€ za let z {city_from}-{from_iata}" \
                       f" do {city_to}-{to_iata}, od {start_date} do {finish_date}. Klikaj {link_for_book}."

        notification_manager = NotificationManager()
        #SEND SMS TO MY NUMBER
        #notification_manager.send_sms(text_message)
        #SEND EMAIL TO ALL REGISTERED USERS WITH FLIGHT INFO
        for user in data_manager.get_user_data():
            user_email = user["email"]
            notification_manager.send_email(text_message, user_email=user_email)
    else:
        print("No flights available.")