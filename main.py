from registration.input_validation import validate_inputs
from registration.duplicate_check import is_duplicate_user
from registration.data_storage import save_user_data
from registration.communication import send_confirmation
from registration.error_handling import handle_error

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

def get_user_input():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    email = input("Enter Email: ")
    return User(username, password, email)

def register_user(user):
    # Step 1: Validate Inputs
    if not validate_inputs(user):
        return handle_error("Validation Error", user)

    # Step 2: Check for Duplicates
    if is_duplicate_user(user):
        return handle_error("User Already Exists", user)

    # Step 3: Save Data
    if not save_user_data(user):
        return handle_error("Database Error", user)

    # Step 4: Send Confirmation
    if not send_confirmation(user.email):
        return handle_error("Failed to Send Confirmation", user)

    return "Registration Successful"

if __name__ == "__main__":
    user = get_user_input()
    result = register_user(user)
    print(result)
