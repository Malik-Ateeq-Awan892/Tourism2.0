import logging
from registration.utils.hashing import hash_password
from registration.utils.database import execute

def save_user_data(user):
    try:
        hashed_password = hash_password(user.password)
        query = "INSERT INTO users (username, password, email) VALUES (?, ?, ?)"
        execute(query, user.username, hashed_password, user.email)
        return True
    except Exception as e:
        logging.error(f"Error saving user data: {e}")
        return False