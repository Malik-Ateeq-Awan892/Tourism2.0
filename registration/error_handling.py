def handle_error(message, user):
    log_error(message, user)
    return message

def log_error(message, user):
    print(f"Error: {message} | User: {user.username} | Email: {user.email}")