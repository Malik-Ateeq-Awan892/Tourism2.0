import re

def validate_inputs(user):
    return is_valid_username(user.username) and is_valid_password(user.password) and is_valid_email(user.email)

def is_valid_username(username):
    return len(username) >= 3

def is_valid_password(password):
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= 8 and has_upper and has_digit

def is_valid_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None