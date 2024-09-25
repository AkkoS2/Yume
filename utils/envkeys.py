import os


def yume_key():
    return os.environ.get("YUME_KEY")


def app_id():
    return os.environ.get("APP_ID")


def loghook():
    return os.environ.get("LOGHOOK")


def typohook():
    return os.environ.get("TYPOHOOK")


def sugghook():
    return os.environ.get("SUGGHOOK")


def cats_key():
    return os.environ.get("CAT_API")


def dogs_key():
    return os.environ.get("DOG_API")
