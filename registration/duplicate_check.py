from registration.utils.database import query

def is_duplicate_user(user):
    query_string = "SELECT COUNT(*) FROM users WHERE username = ? OR email = ?"
    result = query(query_string, user.username, user.email)
    return result > 0