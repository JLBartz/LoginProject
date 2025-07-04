def load_users(filename="users.txt"):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    username, password = parts
                    users[username.strip()] = password.strip()
    except FileNotFoundError:
        print("User file not found.")
    return users

def validate_user(username, password, filename="users.txt"):
    users = load_users(filename)
    return users.get(username) == password
