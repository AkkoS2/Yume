import os


def yume_key():
    return os.environ.get("YUME_KEY")


def app_id():
    return os.environ.get("APP_ID")
