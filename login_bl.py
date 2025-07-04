from login_dal import get_users

def authenticate(username, password):
    """
    Checks if the provided username and password match any user in the data source.
    Returns True if credentials are valid, False otherwise.
    """
    users = get_users()
    for user, pwd in users:
        if user == username and pwd == password:
            return True
    return False