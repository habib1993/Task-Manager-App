import json
import os

DATA_DIR = "data"


def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)


def get_users_file():
    ensure_data_dir()
    return os.path.join(DATA_DIR, "users.json")


def get_task_file(username):
    ensure_data_dir()
    return os.path.join(DATA_DIR, f"tasks_{username}.json")


def load_json(file):
    try:
        if not os.path.exists(file):
            return {} if "users" in file else []
        with open(file, "r") as f:
            return json.load(f)
    except:
        return {} if "users" in file else []


def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)