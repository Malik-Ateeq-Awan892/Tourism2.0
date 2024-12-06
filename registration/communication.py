from registration.utils.email import send_email

def send_confirmation(email):
    subject = "Welcome to Our Platform!"
    body = "Thank you for registering. Please confirm your email."
    return send_email(email, subject, body)