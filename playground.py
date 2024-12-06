from registration.input_validation import is_valid_username, is_valid_password, is_valid_email
from registration.communication import send_confirmation
from registration.data_storage import save_user_data
from main import User 
from registration.duplicate_check import is_duplicate_user
from registration.error_handling import handle_error
from place.place_db import insert_place, read_places, Create_places_table

# print(is_valid_password("Ateeqawan892@gmailcom"))
# print(send_confirmation("ateeqawan"))
#user1= User("name","password","email")
#user2= User("name","password","email")
"""print(save_user_data(user1))
print(save_user_data(user2))
print(is_duplicate_user(user1))
print(is_duplicate_user(user2))
print(handle_error("abc",user1))
"""
Create_places_table()
insert_place("hunza", "des", "gb", 3)
places = read_places()
print(places)