import hashlib
from storage import load_json, save_json, get_users_file


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    if not username or not password:
        return False, "Fields cannot be empty"

    users = load_json(get_users_file())

    if username in users:
        return False, "User already exists"

    users[username] = hash_password(password)
    save_json(get_users_file(), users)

    return True, "Registered successfully"


def login_user(username, password):
    users = load_json(get_users_file())
    return username in users and users[username] == hash_password(password)